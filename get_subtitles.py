import struct, os, sys, subprocess
from xmlrpclib import ServerProxy,ProtocolError

MOVIE_FORMATS = ['avi','mkv']

def getMovieHash(movie):
    longlongformat = 'Q'
    bytesize = struct.calcsize(longlongformat)
    format = "<%d%s" % (65536//bytesize, longlongformat)
    f = open(movie,'rb')
    filesize = os.fstat(f.fileno()).st_size
    hash = filesize

#if filesize < 65536 * 2:
#    return "SizeError"

    buffer= f.read(65536)
    longlongs= struct.unpack(format, buffer)
    hash+= sum(longlongs)
    f.seek(-65536, os.SEEK_END)
    buffer= f.read(65536)
    longlongs= struct.unpack(format, buffer)
    hash+= sum(longlongs)
    hash&= 0xFFFFFFFFFFFFFFFF
    f.close()
    returnedhash =  "%016x" % hash
    return (returnedhash,filesize)

if len(sys.argv) < 2:
    sys.exit()

directory = sys.argv[1]

videos = []
for f in MOVIE_FORMATS:
    res = subprocess.Popen(['find',directory,'-name','*%s'%f],stdout=subprocess.PIPE).communicate()[0]
    if res != '':
        videos.extend(res.split('\n'))

#remove empty strings from list
videos = filter(lambda x: x != '', videos)
print videos


s = ServerProxy('http://api.opensubtitles.org/xml-rpc', allow_none=True)
try:
    res = s.LogIn('peddromcaraujo','mxxxsz','SubDownloader','2.0.10')
except ProtocolError:
    print "Opensubtitles.org is probably overloaded. Give it some time....."
    sys.exit()

# [{'moviebytesize': '366786266', 'sublanguageid': 'eng', 'moviehash': 'dcb7dbae558c63f6'}, {'moviebytesize': '576700632', 'sublanguageid': 'eng', 'moviehash': 'f2671cfa1d9ece6f'}]

query = []
for video in videos:
    returnedhash,filesize = getMovieHash(video)
    query.append({'moviehash':returnedhash,'sublanguageid':'eng','moviebytesize':str(filesize)})

print query

print s.SearchSubtitles(res['token'],query)

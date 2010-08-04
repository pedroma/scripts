import struct, os

longlongformat = 'Q'
bytesize = struct.calcsize(longlongformat)
format = "<%d%s" % (65536//bytesize, longlongformat)
f = open('Lie.to.Me.S02E18.HDTV.XviD-LOL.[VTV].avi','rb')
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

from xmlrpclib import ServerProxy
s = ServerProxy('http://api.opensubtitles.org/xml-rpc',allow_none=True)
res = s.LogIn('peddromcaraujo','mxxxsz','SubDownloader','2.0.10')

# [{'moviebytesize': '366786266', 'sublanguageid': 'eng', 'moviehash': 'dcb7dbae558c63f6'}, {'moviebytesize': '576700632', 'sublanguageid': 'eng', 'moviehash': 'f2671cfa1d9ece6f'}]

query = [{'moviehash':returnedhash,'sublanguageid':'eng','moviebytesize':str(filesize)}]
print query,res['token']

print s.SearchSubtitles(res['token'],query)

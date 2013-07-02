#!/bin/bash
#s bash script will resize all files used by ImageMagick
#to a maximum size specified below. It will retain the
#proportions (width versus height) of your files, while
#shrinking them. Before doing any resizing, it will backup
#each picture to a backup folder within the current directory
#(which it will create, if the backup folder does not already
#exist).

#change these variables to the maximum dimensions you want for your pictures
xsize=1280
ysize=760
##############################################
#Don't touch below here unless you know what you're doing.

filelist=$(find ./ -maxdepth 1 -type f)
#debug echo $filelist

for filename in $filelist ; do
if identify $filename >& /dev/null ; then
info=$(identify $filename 2> /dev/null)
dimensions=$(echo ${info#*.} | awk '{print $3}')
#debug echo "The dimensions are: " $dimensions "for file " $filename
xdim=$(echo ${dimensions%x*})
ydim=$(echo ${dimensions#*x})
#debug echo "xdim for $filename is $xdim"
#debug echo "ydim for $filename is $ydim"
if [ $xdim -gt $xsize -o $ydim -gt $ysize ] ; then
echo "$filename has dimensions greater than "$xsize"x"$ysize
if ! [ -d ./backupPictures ] ; then
mkdir ./backupPictures
echo "Found no backup directory, creating backupPictures"
# else
#debug echo "Found backup directory"
fi

filename=$(echo ${filename#./})

if mv $filename "./backupPictures/$filename" ; then
echo "$filename backed up to ./backupPictures/$filename"
if convert "./backupPictures/$filename" -resize $xsize"x"$ysize $filename ; then
echo "$filename has been resized"
fi
fi


fi

fi

done

#!/bin/bash
WATERMARK="$HOME/Pictures/watermark/watermark.jpg"

echo "*****************************************"
echo "* Image Resize and Watermarking Script  *"
echo "* By Gilbert Mendoza -  SavvyAdmin.com! *"
echo "*****************************************"
echo " "

for each in `ls ~/Pictures/temp/*{.jpg,.jpeg,.png}`
 do
  echo "Working on $each ..."
  convert -resize 440 $each $each 
  composite -gravity northeast -dissolve 15.3 $WATERMARK $each $each
  echo "... Done!"
 done
exit 0

#!/bin/bash

for image in `ls /home/hj/raw_image/random-cviu-5/`
do
	echo "/home/hj/raw_image/random-cviu-5/$image" >> random-cviu-5.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done
for image in `ls /home/hj/raw_image/random-cviu-15/`
do
	echo "/home/hj/raw_image/random-cviu-15/$image" >> random-cviu-15.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done


echo "finish train set"

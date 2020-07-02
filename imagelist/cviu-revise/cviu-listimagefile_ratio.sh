#!/bin/bash

for image in `ls /home/hj/raw_image/random-cviu-15_ratio/`
do
	echo "/home/hj/raw_image/random-cviu-15_ratio/$image" >> random-cviu-15_ratio.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done

echo "finish train set"

#!/bin/bash

for image in `ls /home/hj/raw_image/cara_ratio/train`
do
	echo "/home/hj/raw_image/cara_ratio/train/$image" >> cara_train_ratio.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done

for image in `ls /home/hj/raw_image/cara_ratio/test`
do
	echo "/home/hj/raw_image/cara_ratio/test/$image" >> cara_test_ratio.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done


for image in `ls /home/hj/raw_image/carb_ratio/train`
do
	echo "/home/hj/raw_image/carb_ratio/train/$image" >> carb_train_ratio.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done


for image in `ls /home/hj/raw_image/carb_ratio/test`
do
	echo "/home/hj/raw_image/carb_ratio/test/$image" >> carb_test_ratio.txt #`echo $image | awk -F '-' '{for (i=1;i<2;i++)print $i}'`" >> ../imagelist/cvltrain.txt
	
done


echo "finish train set"

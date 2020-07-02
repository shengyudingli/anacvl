#!/usr/bin/env python

import random
import sys

filename = sys.argv[1]
print filename
f = open(filename)

arr = []

for lines in f.readlines():
	arr.append(lines)

f.close()
random.shuffle(arr)
for lines in arr:
	print lines

ff = open(filename,'w')
for i in arr:
	ff.write(i)
ff.close()

#!/usr/bin/env python
# Script returns new songs in folder or on mp3 player
# Used in combination with add songs 

import os
from glob import glob
from random import randrange
from re import search
from re import sub
print "Checking difference in mp3 files"
# append mp3 files in current working directory to a list
currentFiles=glob('*.mp3')
os.chdir("/media/bao/0123-4567/MUSIC")
sansaFiles=glob('*.mp3')
diffFiles=[]
present=False

for i in currentFiles:
	for x in sansaFiles:
		if(i==x):
			present=True
	#Add file to list if it differs
	if present==False:
		diffFiles.append(i)
	#Reset value for 'present'
	present=False

for i in diffFiles:
	print diffFiles



#!/usr/bin/env python
# Script removes random numbers in front of mp3's

import os
from glob import glob
from random import randrange
from re import search
from re import sub
print "Would you like to remove random numbers in front of mp3 files (y/n)?"
runChoice=raw_input("> ")
if runChoice=="y":
	# append mp3 files in current working directory to a list
	currentFiles=glob('*.mp3')

	for i in currentFiles:
		#replace random # if it already exists in front of file
		if(search("^[0-9]*_",i)!=None):
			dupName=sub("^[0-9]*_","", i)
			os.rename(i,dupName)
	print "Successfully renamed mp3's"
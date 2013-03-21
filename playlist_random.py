#!/usr/bin/env python
# Script adds random number in front of mp3 files each time it is called
# to improve playlist randomness

import os
from glob import glob
from random import randrange
from re import search
from re import sub
print "Would you like to randomize mp3 files (y/n)?"
runChoice=raw_input("> ")
if runChoice=="y":
	# append mp3 files in current working directory to a list
	currentFiles=glob('*.mp3')

	for i in currentFiles:
		#replace random # if it already exists in front of file
		if(search("^[0-9]*_",i)!=None):
			dupName=sub("^[0-9]*_",str(randrange(100))+"_", i)
			os.rename(i,dupName)
		#else add a random # in front of file
		else: 
			rName="0"+str(randrange(100))+"_"+i
			os.rename(i,rName)
	print "Successfully randomized mp3's"
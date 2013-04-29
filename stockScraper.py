#!/usr/bin/env python
# Script downloads CSV file from a scraper to pull data from NASDAQ's Akamai company
# Author: Sebastien Luong
import urllib2

url="https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=csv&name=akamai&query=select+*+from+`swdata`&apikey="

print "Saving Akamai CSV file....."

f = urllib2.urlopen(url)
data=f.read()
with open("stocks.csv", "wb") as code:
	code.write(data) 

print "Ding! Enjoy!"
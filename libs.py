#!/usr/bin/python

import csv
import string
import sys



def splitCategoriesConnections( catconn ):
	categories = []
	connections = []

	items = catconn.split(' ')
	for i in items:
		if i[:1] == '#':
			categories.append(i)
		elif i[:1] == '@':
			connections.append(i)
		else:
			if i != "":
				print >> sys.stderr, "Fix untagged: "+ i

	return categories, connections

def getYTID(url):
	id = string.replace(url, 'https://www.youtube.com/watch?v=','')
	return id


def getCSV(datafile):
	data = []
	with open(datafile, "rb") as file:
		c = csv.reader(file)
		for row in c:
			data.append(row)

	return data

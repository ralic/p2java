#!/usr/bin/python

import sys

def changeme(mylist):
	## This change s a pssed list into this function"
	mylist.append([1,2,3,4])
	# print mylist
	return mylist

mylist=[2,4,6,8]
print mylist

newlist=changeme(mylist)
print newlist
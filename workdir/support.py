#!/usr/bin/python

import sys

fh=open("testfile",'r+')
fh.write("hello\n")
fh.close();

fh2=open("testfile",'a')
fh2.write("hello2\n")
fh2.close()
#!/usr/bin/python

import sys

# print "Command Line Argument for ",sys.argv[0]

# print str(sys.argv)

# a= sys.argv[1]
# b= sys.argv[2]

# print int(a)+int(b)

# print "Completed [ " + sys.argv[0] , "]"

name = sys.argv[1];
age = sys.argv[2];
# print name
print name,age

# def happyBirthdayEmily(): #program does nothing as written
#     print("Happy Birthday to you!")
#     print("Happy Birthday to you!")
#     print("Happy Birthday, dear Emily.")
#     print("Happy Birthday to you!")

# happyBirthdayEmily()

# "This prints a passed info into this function"

def printinfo ( name , age) :
		print "Name : ", name;
		print "Age " , age;
		return;

	# "This prints a passed info into this function"
def printinfo ( name , age=35) :
		print "Name : ", name;
		print "Age " , age;
		return name;

dog_owner=printinfo('ralic');

print "Dog belongs to",dog_owner


def f():
    print('In function f')

print('When does this print?') ## Print Before f()

f()
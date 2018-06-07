#!/usr/bin/env python

x = raw_input('Enter the first integer: ')
y = raw_input('Enter the second integer: ')

if int(x) > int(y):
    print "The maximum is", x
    sub = int(x)- int(y)
else:
    print "The maximum is", y
    sub = int(y) - int(x)


if int(x) < int(y):
    print "The minimum is", x
else:
    print "The minimum is", y
  

print "Maximum - minimum equals ", sub

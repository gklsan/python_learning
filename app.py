#!/usr/bin/python

import sys

# printing hello there
print("hello there!")

# This is single line comment
# print(sys.version)

"""
This is multiline comments in python
"""
print('After the comments')

## variables
a = 'string'
print(type(a), a)
a = 1
print(type(a), a)
a = 1.0
print(type(a), a)

#string casting
a = str(1)
print(type(a), a)
a = int(1)
print(type(a), a)
a = float(1)
print(type(a), a)

myvar = 'myvar'
my_var = 'my_var'
_myvar = '_myvar'
myVar = 'myVar'
MY_VAR = 'MY_VAR'
MYVAR = 'MYVAR'
MYVAR = 'MYVAR'
my_var1 = 'my_var1'
print(myvar, my_var, _myvar, myVar, MY_VAR, MYVAR, my_var1)
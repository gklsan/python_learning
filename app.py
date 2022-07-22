#!/usr/bin/python

import sys
import random

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

# multiple values assignment
a, b, c = 1, 2, 3
print(a, b, c)

a, b, c = [4, 5, 6]
print(a, b, c)

a = b = c = 'values'
print(a, b, c)

a = 1

print(b + c, a)



def myFun():
    global x
    x = 'Global variable'
    y = 'Local variable'
    print('This is myFun', a)
    print('This is ' + x)

myFun()
print(x)

def printType(input):
    print(type(input), input)

printType(1j)
printType([])
printType(range(5))
printType({})
printType({a: 1, 'b': 2, 3: 4, })
printType(dict({'name': 1, 'b': 2, 3: 4, }))
printType({a, b})
printType({a, b, 4})
printType(frozenset({a: 1}))
printType(frozenset({a, b, 4}))
printType(True)
printType(False)

# print random number
printType(random.randrange(10))
printType(random.randrange(7, 10))


# Integer array
input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(input[2])
print(input[2:6])
print(input[12:])
print(input[:7])
print(input[:-5])


# String
input = 'Here is the input text '
print('String', input[2])
print(input[2:6])
print(input[12:])
print(input[:7])
print(input[:-5])

def simple_print(txt, input):
    print(txt, ': ', input)

simple_print('Uppercase', input.upper())
simple_print('Lowercase', input.lower())
simple_print('strip', input.strip())

txt = 'Hello {}'

name = 'gokul'.upper()
welcome = 'welcome!'
simple_print('String' , txt.format(name))

txt = 'Hello {} {}'
simple_print('String' , txt.format(name.upper(), welcome))

txt = 'Hello {1} {0}'
simple_print('String' , txt.format(name.upper(), welcome))

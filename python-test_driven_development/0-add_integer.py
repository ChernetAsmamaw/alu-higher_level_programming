#!/usr/bin/python3
'''
This is the "0-add_integer" module
The module supplies one function, add_integer(a, b)
'''

def add_integer(a, b=98):
    ''' this function returns the addtion of two numbers'''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a+b)

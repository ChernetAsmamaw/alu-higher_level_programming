#!/usr/bin/python3
'''
This is the "4-print_square" module.
The module supplies one function, print_square(size).
'''


def print_square(size):
    '''prints a square with the character #'''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

#!/usr/bin/python3
# Returns a tuple with 2 integers
# The 1st element is an addition of each of the 1st arguments & same for the 2nd
#Tuple smaller than2 use 0 and for tupler bigger than 2 use first 2 intigers


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    suma1 = tuple_a[0] + tuple_b[0]
    suma2 = tuple_a[1] + tuple_b[1]
    return (suma1, suma2)

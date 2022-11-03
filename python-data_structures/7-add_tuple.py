#!/usr/bin/python3
# Returns a tuple with 2 integers
# The first element is an addition of each of the first arguments and same for the second
# If the tuple is smaller than 2 use 0 for each missing intiger and if it's more than 2 use the first 2 intigers


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    suma1 = tuple_a[0] + tuple_b[0]
    suma2 = tuple_a[1] + tuple_b[1]
    return (suma1, suma2)

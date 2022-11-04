#!/usr/bin/python3
# Returns a list with all values multiplied by a number without using any loops
# Return new list same size as my_list and each value multiplied by number


def multiply_list_map(my_list=[], number=0):
    return list(map((lambda i: i*number), my_list))

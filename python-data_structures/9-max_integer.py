#!/usr/bin/python3
# finds the biggest integer of a list
# if the list is empty it returns None


def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
    else:
        return(None)
    return(my_list[-1])

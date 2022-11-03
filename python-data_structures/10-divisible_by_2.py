#!/usr/bin/python3
# Finds all multiples of 2 in a list
# Return a new list with true of false about the multiplication


def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return(new_list)

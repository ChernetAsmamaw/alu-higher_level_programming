#!/usr/bin/python3
# This function replaces an element from the list with a specific position
# Without modifying the original list


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return new_list
    else:
        new_list[idx] = element
        return new_list

#!/usr/bin/python3
# Deletes the item at a specific position in a list
# If idx is negative or out of range list stays the same


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list - 1)):
        return my_list
    else:
        del my_list[idx]
        return my_list

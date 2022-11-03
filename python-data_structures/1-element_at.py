#!/usr/bin/python3
# The function retrieves an element from the list
# If the idx is negative or out of range it returnes None


def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]

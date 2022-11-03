#!/usr/bin/python3
# replaces an elemnet of a list at a specific position 
# index will be replaced and element replaces the elements in index

def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        my_list = new_list
        return new_list

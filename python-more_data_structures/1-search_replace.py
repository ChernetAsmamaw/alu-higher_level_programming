#!/usr/bin/python3
# In my_list the element search will be replaced by replace


def search_replace(my_list, search, replace):
    new_list = []
    new_list = [replace if i == search else i for i in my_list]
    return new_list

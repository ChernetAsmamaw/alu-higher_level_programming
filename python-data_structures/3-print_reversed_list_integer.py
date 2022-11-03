#!/usr/bin/python3
# Prints all intigers of the list in reverse order
# Can assume that the list only contains intigers


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for a in range(len(my_list)):
            print("{:d}".format(my_list[a]))

#!/usr/bin/python3
# Prints a dictionary by ordered keys sorted in alphabetic order
# Keys of a directory inside the main directory are not sorted


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))

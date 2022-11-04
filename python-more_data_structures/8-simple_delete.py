#!/usr/bin/python3
# Deletes a key in a dictionary
# key argument is a string and if a key doesn’t exist, dictionary won’t change


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

#!/usr/bin/python3
# Replaces or adds key/value in a dictionary
# key argument is a string and value any other type
# If a key exisists the value will be replaced if not it'll be created


def update_dictionary(a_dictionary, key, value):
    val = {key: value}
    a_dictionary.update(val)
    return (a_dictionary)

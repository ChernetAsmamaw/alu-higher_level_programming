#!/usr/bin/python3
""" Add items in a list """

from os import path
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items():
    """
    # Adds all arguments to a Python list, and then save them to a file.
    """

    list_json = []

    """ Check if file exists """
    if path.isfile("add_item.json"):
        list_json = load_from_json_file("add_item.json")

    if len(argv) > 1:

        for i in range(1, len(argv)):
            list_json.append(argv[i])

    """ Write the list with the new elements in the file """
    save_to_json_file(list_json, "add_item.json")


if __name__ == "__main__":
    add_items()

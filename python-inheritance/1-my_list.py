#!/usr/bin/python3
''' A class MyList that inherits from list '''


class MyList(list):
    """create mi class mylist with inheritance"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))

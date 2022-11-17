#!/usr/bin/python3
''' A class MyList that inherits from list '''


class Mylist(list):
    ''' create a Mylist through inheritance '''
    def print_sorted(self):
        ''' Sorts the list an dprints it '''
        print(sorted(self))

#!/usr/bin/python3
# A class MyList that inherits from list


class Mylist(list):

    def print_sorted(self):
        
        # Sorts the list an dprints it
        print(sorted(self))

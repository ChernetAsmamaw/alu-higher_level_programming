#!/usr/bin/python3
# A class MyList that inherits from list


class Mylist(list):

    # This inherits from the superclass
    def __inti__(self):

    # This installs the objects 
    super().__init__()

    def print_sorted(self):
        
        # Sorts the list an dprints it
        print(sorted(self))

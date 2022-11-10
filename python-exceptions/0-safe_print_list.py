#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for add in my_list[:x]:
        try:
            print("{}".format(add), end="")
            i += 1
          except IndexError:
              print()
     print()
     return i

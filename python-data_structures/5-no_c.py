#!/usr/bin/python3
# A function that removes all c and C characters from a string

def no_c(my_string):
    if my_string:
        new_string = list(my_string)
        for i in new_string:
            if i in "cC":
                new_string.remove(i)
                my_string = "".join(new_string)
    return my_string

#!/usr/bin/python3
# A function that removes all c&C characters from a string 


def no_c(my_string):
    word = ""
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            pass
        else:
            word += my_string[i]


    return word

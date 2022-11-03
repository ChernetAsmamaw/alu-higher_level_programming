#!/usr/bin/python3
# Function retieves an element from the list 
# If the value is negative or out of the list's range it returnes None

def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]

#!/usr/bin/python3
# Prints a matricx of intigers 

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matricx)):
        for k in range(len(matricx[i])):
            print("{:d}".format([i][k]), end="")
            if k != len((matrix[i]) - 1):
                print(" ", end="")
        print("")

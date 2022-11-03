#!/usr/bin/python3
# Prints a matricx of intigers


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print()
        else:
            for k in i:
                if k == i[-1]:
                    print("{:d}".format(k))
                else:
                    print('{:d}'.format(k), end=" ")

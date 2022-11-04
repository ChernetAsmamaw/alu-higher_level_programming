#!/usr/bin/python3
# Computes the square value of all integers of a matrix
# Returns a new matrix, each is the square of the value of the input


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    nw_matrix = []
    for row in range(len(matrix)):
        k = [i*i for i in matrix[row]]
        nw_matrix.append(k)
    return nw_matrix

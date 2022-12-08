#!/usr/bin/python3                                                                                                                                       
"""                                                                                                                                                    
This is the "2-matrix_divided" module.                                                                                                                   
The supplies one function, matrix_divided(matrix, div).                                                                                                  
"""                                                                                             
                                                                                                                                                         
                                                                                                                                                        
def matrix_divided(matrix, div):                                                                                                                         
    '''this divides all elements in the matrix by div'''                                                                                               
     if (matrix == [] or matrix == [[]] or
        type(matrix) is not list or
            not all(type(xy) is list for xy in matrix)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    for xy in matrix:
        for element in xy:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if len(xy) != len(matrix[0]):
            raise TypeError("Each xy of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), xy)) for xy in matrix]

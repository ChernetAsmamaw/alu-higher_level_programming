#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    l1 = len(m_a)
    if l1 == 0:
        raise ValueError("m_a can't be empty")
    l2 = None
    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")
        if l2 is None:
            l2 = len(item)
            if l2 == 0:
                raise ValueError("m_a can't be empty")
        if l2 != len(item):
            raise TypeError("each row of m_a must be of the same size")
        for j in item:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    l3 = None
    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")
        if l3 is None:
            l3 = len(item)
            if l3 == 0:
                raise ValueError("m_b can't be empty")
        if l3 != len(item):
            raise TypeError("each row of m_b must should be of the same size")
        for j in item:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for item in range(l1):
        l = []
        for j in range(l3):
            n = 0
            for k in range(l2):
                n += m_a[item][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix

#!/usr/bin/python3
"""matrix divided"""


def matrix_divided(matrix, div):
    """matrix divided"""

    if not isinstance(div, (int, float)):
        raise TypeError("div most be a numebr")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    typerr = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(typerr)

    size = len(matrix[0])

    for item in matrix:
        if not item or not isinstance(item, list):
            raise TypeError(typerr)

        if size != 0 and len(item) != size:
            raise TypeError("Each row of the matrix must have the same size")
        
        for i in item:
            if not isinstance(i, (int, float)):
                raise TypeError(typerr)

    newm = []
    newr = []
    for row in matrix:
        for item in row:
            newr.append(round(item / div, 2))
        newm.append(newr)
        newr = []

    return newm

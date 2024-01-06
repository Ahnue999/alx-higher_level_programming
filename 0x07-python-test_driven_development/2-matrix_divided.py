#!/usr/bin/python3


def matrix_divided(matrix, div):
    """matrix divided"""
    if not matrix:
        return []

    if not isinstance(div, (int, float)):
        raise TypeError("div most be a numebr")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    newm = []
    newr = []
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            newr.append(round(item / div, 2))
        newm.append(newr)
        newr = []

    return newm

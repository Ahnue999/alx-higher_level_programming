#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    new = matrix.copy()
    for i in range(rows):
        new[i] = list(map(lambda x: x ** 2, matrix[i]))

    return (new)

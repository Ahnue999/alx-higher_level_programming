#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    if rows <= 0:
        return
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if j == cols - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if j != 0:
                print("",end=" ")
            print("{:d}".format(matrix[i][j]), end="")
        print()

#!/usr/bin/python3
""" returns a pascal triangle """


def pascal_triangle(n):
    """ returns a pascal triangle """

    if n <= 0:
        return []

    tri = [[1]]

    prev = [0, 1, 0]

    for i in range(n - 1):
        new = []
        for d in range(len(prev) - 1):
            new.append(prev[d] + prev[d + 1])
        tri.append(new)
        prev = [0] + new + [0]

    return (tri)

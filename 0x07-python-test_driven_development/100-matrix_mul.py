#!/usr/bin/python3
""" Matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """ multiplies two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    m_a_cols = len(m_a[0])

    for row in m_a:
        if len(row) != m_a_cols:
            raise TypeError("each row of m_a must be of the same size")

    m_b_cols = len(m_b[0])

    for row in m_b:
        if len(row) != m_b_cols:
            raise TypeError("each row of m_b must be of the same size")

    if m_a_cols != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    newm = []
    for i in range(len(m_a)):
        newr = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += (m_a[i][k] * m_b[k][j])
            newr.append(sum)
        newm.append(newr)
    return (newm)

#!/usr/bin/python3
"""This module contain a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """matrix_mul function that multiplies two matrix
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_cols = 0
    num_rows = 0

    # Check requirements for matrix m_a
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if type(row1) != list:
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if not len1:
            raise ValueError("m_a can't be empty")
        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")
        num_cols = len(row1)
        for column1 in row1:
            if type(column1) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if not len2:
            raise ValueError("m_b can't be empty")
        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")
        num_rows += 1
        for column2 in row2:
            if type(column2) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is posible
    if num_cols != num_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_a in m_a:
        row_result = []
        for col_b in range(len(m_b[0])):
            result = 0
            for i in range(len(row_a)):
                result += row_a[i] * m_b[i][col_b]
            row_result.append(result)
        mul_matrix.append(row_result)

    return mul_matrix

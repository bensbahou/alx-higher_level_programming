#!/usr/bin/python3
"""
pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        triangles.append([1] + [tri[i] + tri[i + 1] for i in range(len(tri) - 1)] + [1])
    return triangles

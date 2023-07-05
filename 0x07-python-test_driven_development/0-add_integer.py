#!/usr/bin/python3
"""
The 0-add_integer module contains a single function called add_integer(a, b).
This function takes two arguments, a and b, and returns their sum as an integer
"""


def add_integer(a, b):
    """Return the addition of two numbers."""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

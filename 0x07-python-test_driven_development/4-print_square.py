#!/usr/bin/python3
"""
The 4-print_square module contains a single function called print_square.
This function takes a single integer argument, size, and prints a square
with "#"s that has a length of size.
"""


def print_square(size):
    """prints a square with "#"'s that has a length of size"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print("\n".join(["#" * size] * size), end="\n")

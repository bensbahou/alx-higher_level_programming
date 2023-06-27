#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class with a private attribute - size."""

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): Size of a side of the square
        Returns: None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

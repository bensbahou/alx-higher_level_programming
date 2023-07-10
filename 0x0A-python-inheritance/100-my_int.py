#!/usr/bin/python3
"""
MyInt module
"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other

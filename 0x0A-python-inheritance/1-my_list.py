#!/usr/bin/python3
"""
MyList module with a class MyList that inherits from list
"""


class MyList(list):
    """MyList class that inherits from list"""

    def __init__(self):
        """initializes MyList"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))

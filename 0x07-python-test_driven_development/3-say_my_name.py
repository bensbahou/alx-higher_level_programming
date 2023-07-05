#!/usr/bin/python3
"""
The 3-say_my_name module contains a single function called say_my_name.
This function takes a first name and an optional last name, and prints
"My name is" followed by the first name and optional last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by the first name and optional last name"""
    
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)

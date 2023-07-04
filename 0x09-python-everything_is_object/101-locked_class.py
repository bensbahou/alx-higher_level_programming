#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    This class restricts the creation of new attributes
    for instances of the class to only 'first_name'.
    It uses `__slots__` to define a list of allowed
    attribute names and save memory by preventing
    the creation of a `__dict__` attribute for each instance."""

    __slots__ = ["first_name"]

#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """Base class for all other classes in this project.
    Args:
        id (int): The identity of the new Base instance.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return serializable representation of list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

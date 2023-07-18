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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects
        to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        with open(cls.__name__ + ".json", "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(100, 100)
            else:
                new = cls(100)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        """
        try:
            with open(str(cls.__name__) + ".json", "r") as jsonfile:
                return [cls.create(**d)
                        for d in Base.from_json_string(jsonfile.read())]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        with open(cls.__name__ + ".csv", "w", newline="") as csv_file:
            if not list_objs:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    head = ["id", "width", "height", "x", "y"]
                else:
                    head = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=head)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        """
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    head = ["id", "width", "height", "x", "y"]
                else:
                    head = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=head)
                list_dicts = [
                    dict([key, int(value)] for key, value in dict_.items())
                    for dict_ in list_dicts
                ]
                return [cls.create(**dict_) for dict_ in list_dicts]
        except IOError:
            return []

#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            id (int): The identity of the new Square.
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): Attributes to update.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Override the default Square string representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

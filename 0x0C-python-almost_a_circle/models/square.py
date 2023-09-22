#!/usr/bin/python3
"""the square module"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """THE SQUARE MODULE THAT INHEREITS FROM RECTANGLE"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor for the square class

        Args:
            size ([int]): [the size of the square which is width/height]
            x (int, optional): [the position x]. Defaults to 0.
            y (int, optional): [the position y]. Defaults to 0.
            id ([int], optional): [the id]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the str representaion"""
        return (
            f"[square] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
            )

    @property
    def size(self):
        """the size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.hegith = value

    def update(self, *args, **kwargs):

        """handling args and kwargs"""
        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            only_attrs = ["id", "size", "x", "y"]
            size_attrs = ["width", "height"]

            for k, v in kwargs.items():
                if k in only_attrs:
                    if k == "size":
                        for size in size_attrs:
                            setattr(self, k, v)
                            continue
                    setattr(self, k, v)

    def to_dictionary(self):
        """the dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

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

#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """the class constructor

        Args:
            width ([int]): the width of the rectangle
            height ([int]): teh rectangle's height
            x (int, optional): [x position]. Defaults to 0.
            y (int, optional): [y positoin]. Defaults to 0.
            id ([int], optional): [the id of every object
                created]. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width geter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width to a spesific value"""
        self.__width = value

    @property
    def height(self):
        """the height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """the x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the x to value"""
        self.__x = value

    @property
    def y(self):
        """the x getter"""
        return self.__y
    @y.setter
    def y(self, value):
        """setting the y to value"""
        self.__y = value

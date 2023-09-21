#!/usr/bin/python3
"""rectangle module"""


from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """AI is creating summary for __init__

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
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
        self.__height
    
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
    
    def y(self, value):
        """setting the y to value"""
        self.__y = value

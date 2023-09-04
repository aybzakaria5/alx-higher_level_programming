#!/usr/bin/python3
"""This module defines a Rectangle with it's operactions"""


class Rectangle:
    """
        a class that define a rectangle:

        Args:
            width(int): int
            weight(int): int

        Raises:
            TypeError: not an integer
            ValueError: if it's less than
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the widht of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """setting the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """gets the height of a rectangle"""

        return self.__height

    @height.setter
    def height(self, value: int):
        """sets the height of the ractangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
            for calculating the area of a rectangle


            Return:
                area = width * height
        """

        return self.__width * self.__height

    def perimeter(self):
        """
            for calculating the perimeter

            Return:
                per = (width + height) * 2
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.height) * 2

    def __str__(self):
        """printing the rectangle using the #"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for i in range(self.__height):
            rec += str(self.print_symbol) * self.__width
            if i != (self.__height - 1):
                rec += "\n"
        return rec

    def __repr__(self):
        """returns a string as representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prenting a message when a rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

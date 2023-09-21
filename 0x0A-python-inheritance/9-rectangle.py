#!/usr/bin/python3
"""currently empty class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """the constructer

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle

        Returns:
            rectangle's area
        """
        return self.__width * self.__height

    def __str__(self):
        """rectnagle

        Returns:
            info
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

#!/usr/bin/python3
"""Square class file bsed on 2-square.py"""


class Square:
    """
    class Square that defines a square

    Attributes:
        __size: size of a side of the square
    """

    # initialisation of an object size
    def __init__(self, size=0):
        """
        Init a square

        Args:
            size (int): size of the square

        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        the area of sqaure

        Returns:
        the square area
        """
        return self.__size * self.__size

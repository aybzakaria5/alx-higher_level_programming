#!/usr/bin/python3
"""Square class file bsed on 4-square.py"""


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

    @property
    def size(self):
        """
        retrive the private size of the squre
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Init a square

        Args:
            size (int): size of the square

        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        prints the stdout the # square
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if not self.__size:
            print()

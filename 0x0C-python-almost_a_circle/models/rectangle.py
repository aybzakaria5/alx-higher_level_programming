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
        """checking width"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        """checking height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        """checking x"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        """checking y"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """width geter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width to a spesific value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """the height getter"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the x to value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the x getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the y to value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """a methode that returns the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """methode to display w * h rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

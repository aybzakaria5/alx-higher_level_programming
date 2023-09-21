#!/usr/bin/python3

"""A BAse Module"""


class Base:
    """a base class to ihneret from"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

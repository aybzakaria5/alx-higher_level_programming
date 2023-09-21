#!/usr/bin/python3
"""This Is A Base Module """


class Base:
    _nb_objects = 0

    def __init__(self, id=None):
        """the constructor of the modue base"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

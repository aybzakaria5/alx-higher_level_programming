#!/usr/bin/python3

"""A BAse Module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """a methode that serialize a data using json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

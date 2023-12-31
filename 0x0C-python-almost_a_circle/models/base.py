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

    @staticmethod
    def from_json_string(json_string):
        """deserilize using json"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """serilize using jsong"""
        if list_objs is None:
            list_objs = []
        filepath = "{}.json".format(cls.__name__)
        json_string = Base.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
        with open(filepath, 'w') as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attributes already set '''
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        if cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loading from a file if exists"""
        filepath = "{}.json".format(cls.__name__)

        try:
            with open(filepath, 'r') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                instance_list = [cls.create(**dict_obj) for
                                 dict_obj in dict_list]
                return instance_list
        except FileNotFoundError:
            return []

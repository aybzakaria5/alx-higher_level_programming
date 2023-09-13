#!/usr/bin/python3
"""This module contains Student class
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of a student"""
        return self.__dict__

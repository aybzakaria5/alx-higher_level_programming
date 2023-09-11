#!/usr/bin/python3
"""module for chccking if class"""


def is_same_class(obj, a_class):
    """
        a fucntion that chacks if the i=object is
        an instance of a specified class
    """

    return type(obj) is a_class

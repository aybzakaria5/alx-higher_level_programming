#!/usr/bin/python3
"""a module to chack if the object is ihnereted"""


def inherits_from(obj, a_class):
    """ chacks if it is a subclass
    this is exactly like using
    issubclass(type(obj), a_class)
    """

    return isinstance(obj, a_class) and type(obj) != a_class

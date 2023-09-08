#!/usr/bin/python3

"""a fcuntion that prints both of last and first name"""


def say_my_name(first_name, last_name=""):
    """a function that prints the first and last name

    Args:
        first_name (str): the first name that must be a string
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: it says that first name must be string
        TypeError: same as the first name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

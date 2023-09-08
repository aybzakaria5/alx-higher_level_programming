#!/usr/bin/python3
"""a function that prints a square"""


def print_square(size):
    """
        a function that prints square with the character #

    Args:
        size (int): size of the square

    Raises:
        ValueError: if the size is less than 0
        TypeError:
    """
    if not (isinstance(size, int) or (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

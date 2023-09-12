#!/usr/bin/python3
"""
Module doc
"""


class MyInt(int):
    """
    a class
    """

    def __eq__(self, other):
        """
        equanlity
        """
        return self.real != other

    def __ne__(self, other):
        """
        inequality
        """
        return self.real == other

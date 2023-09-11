#!/usr/bin/python3
"""a class for returning a list"""


class MyList(list):
    """a class that inherets the list"""
    def print_sorted(self):
        """printing the sorted list"""

        print(sorted(self))
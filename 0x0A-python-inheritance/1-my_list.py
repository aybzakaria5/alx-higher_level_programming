#!/usr/bin/python3
"""a class for returning a list"""


class MyList(list):
    """a class that inherets the list"""
    def print_sorted(self):
        """printing the sorted list"""
        n = len(self)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self[j] > self[j+1]:
                    self[j], self[j+1] = self[j+1], self[j]
        return self


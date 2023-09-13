#!/usr/bin/python3
"""reading a file"""


def read_file(filename=""):
    """
        a fucntion that reads a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
        f.closed

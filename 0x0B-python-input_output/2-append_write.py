#!/usr/bin/python3
"""a function to append data"""


def append_write(filename="", text=""):
    """appends the data ti a file"""

    with open(filename, "a", encoding="utf-") as f:
        return f.write(text)

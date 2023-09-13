#!/usr/bin/python3
"""writing an object to a text file using json"""

import json


def save_to_json_file(my_obj, filename):
    """serialize the boject to text file using JSON representation

    Args:
        my_obj: object
        filename: file's name

    Returns:
        serialized text
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)

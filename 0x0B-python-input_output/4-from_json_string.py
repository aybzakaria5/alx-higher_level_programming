#!/usr/bin/python3
"""using json module"""

import json


def from_json_string(my_str):
    """from json string to an object

    Args:
        my_str (_type_): a json string
    Return:
        object
    """
    return json.loads(my_str)

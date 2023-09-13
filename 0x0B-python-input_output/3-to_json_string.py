#!/usr/bin/python
"""using json module"""

import json


def to_json_string(my_obj):
    """returns the json representation of the objct

    Args:
        my_obj (_type_): an object
    Return:
        a JSON representation
    """
    return json.dumps(my_obj)

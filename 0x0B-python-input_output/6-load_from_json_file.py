#!/usr/bin/python3
'''module to create a an object from json file
'''


import json


def load_from_json_file(filename):
    ''' objct to json file
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f.read()))

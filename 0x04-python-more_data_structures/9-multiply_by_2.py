#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in list(new_dictionary.keys()):
        new_dictionary[key] *= 2
    return new_dictionary

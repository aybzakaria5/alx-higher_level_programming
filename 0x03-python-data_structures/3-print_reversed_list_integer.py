#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in range(len(my_list)):
            """using Slicing OPerator , we can use the reverse() methode"""
            rev = my_list[::-1][i]
            print("{:d}".format(rev))

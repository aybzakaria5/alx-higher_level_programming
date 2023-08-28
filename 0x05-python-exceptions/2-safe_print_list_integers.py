#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
            """handling the ValueError
            and TYpeError and ignoe it"""
        except (ValueError, TypeError):
            pass

    print("")
    return counter

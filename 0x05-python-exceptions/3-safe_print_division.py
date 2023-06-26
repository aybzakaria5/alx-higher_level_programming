#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
        """ignors the zero division error
        and excuting what is in
        the finally block anyway"""
    except ZeroDivisionError:
        div = None
    else:
        return div
    finally:
        print("Inside result: {}".format(div))

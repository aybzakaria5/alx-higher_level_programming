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
    finally:
        print("inside result: {}".format(div))
        return div

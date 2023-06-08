#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    len = len(sys.argv) - 1
    """excluding the programme's name"""
    if len == 0:
        print("0 arguments.")
    elif len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len))
    for i in range(len):
        print("{}: {}".format(i + 1, sys.argv[i+1]))

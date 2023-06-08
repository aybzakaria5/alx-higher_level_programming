#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    import sys
    count = len(sys.argv)
    if count - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    """using dictionaries"""
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] in list(operators.keys()):
        print("{} {} {} = {}".format(a, sys.argv[2], b,
                                     operators[sys.argv[2]](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

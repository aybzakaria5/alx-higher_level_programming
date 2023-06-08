#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum0 = 0
    n = len(sys.argv)
    for i in range(n - 1):
         sum0 += int(sys.argv[i + 1])
    print("{}".format(sum0))

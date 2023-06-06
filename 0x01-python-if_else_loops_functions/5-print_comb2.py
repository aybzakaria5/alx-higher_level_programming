#!/usr/bin/python3
for nbr in range(0, 100):
    if nbr == 99:
        print("{}".format(nbr))
    else:
        print("{:02}".format(nbr), end=", ")

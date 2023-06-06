#!/usr/bin/python3
for ltr in range(97, 123):
    if chr(ltr) is not 'e' and chr(ltr) is not 'q':
        print("{}".format(chr(ltr)), end="")

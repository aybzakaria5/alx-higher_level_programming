#!/usr/bin/python3

nonprint_letters = ['q', 'e']
for letter in range(97, 123):
    if chr(letter) not in nonprint_letters:
        print("{}".format(chr(letter)), end="")

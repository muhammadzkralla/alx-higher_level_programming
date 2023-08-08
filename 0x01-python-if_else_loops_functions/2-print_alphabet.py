#!/usr/bin/python3
"""print the alphabets from a to z."""

for letter in range(ord('a'), ord('a') + 26):
    print("{}".format(chr(letter)), end="")


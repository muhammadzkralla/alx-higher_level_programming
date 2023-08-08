#!/usr/bin/python3
"""Print the Alphabets without 'q' & 'e'"""

for letter in range(ord('a'), ord('a') + 26):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")

#!/usr/bin/python3
"""Function to remove a certain char from string"""


def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string

    result = ""
    for i in range(len(string)):
        if i != n:
            result += string[i]

    return result

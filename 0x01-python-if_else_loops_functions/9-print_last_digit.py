#!/usr/bin/python3
"""Function get the last digit in a given number"""


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)

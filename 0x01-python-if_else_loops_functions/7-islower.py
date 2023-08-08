#!/usr/bin/python3
"""Check if char is lowercase"""

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

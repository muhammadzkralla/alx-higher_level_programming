#!/usr/bin/python3
"""Print all numbers from 1 to 100 in 02 format"""

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")

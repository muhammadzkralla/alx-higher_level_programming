#!/usr/bin/pyhton3
"""A function that prints numbers from 1 to 100 but with a simple transformation"""


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end = "")
        elif (i % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")

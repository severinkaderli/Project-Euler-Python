#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 5:
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
from functools import reduce

def gcd(a, b):
    """Returns the greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    "Returns the lowest common multiple."
    return a * b // gcd(a, b)

def lcmm(*args):
    "Returns the lcm of multiple numbers."
    return reduce(lcm, args)  

if __name__ == "__main__":
    print(lcmm(*range(11, 21)))
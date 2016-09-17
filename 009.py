#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 9:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def get_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000 - a):
            for c in range(b + 1, 1000 - b):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a * b * c

    return 0

if __name__ == "__main__":
    print(get_pythagorean_triplet())

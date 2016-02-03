#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 1:
# Find the sum of all the multiples of 3 or 5 below 1000.
def get_sum(limit = 1000):
    """Gets the sum of the multiples of 3 or 5"""
    sum = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

if __name__ == "__main__":
    print(get_sum())

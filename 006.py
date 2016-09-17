#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 6:
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
def calculate_sum_square_difference(n):
    """Gets the difference between the squared sum and the sum of squares."""
    square_sum = 0
    sum = 0

    for i in range(1, n + 1):
        square_sum += i**2
        sum += i

    return sum**2 - square_sum

if __name__ == "__main__":
    print(calculate_sum_square_difference(100))

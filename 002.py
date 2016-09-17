#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 2:
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
def fib():
    """Generator for generating fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_sum(limit = 4000000):
    """Get the sum of the even fibonacci numbers"""
    sum = 0
    fibonacci_sequence = fib()
    for n in fibonacci_sequence:
        if n > limit:
            break;
        if n % 2 == 0:
            sum += n
    return sum

if __name__ == "__main__":     
    print(get_sum())

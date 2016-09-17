#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 7:
# What is the 10 001st prime number?
def is_prime(n):
    """Checks if a number is a prime number."""
    if n <= 2: return False
    if n % 2 == 0: return False

    i = 3
    while i < n**0.5+1:
        if n % i == 0: return False
        i += 2

    return True

def get_prime_number(n):
    """Gets the nth prime number."""
    prime = 2
    count = 1

    i = 3
    while count < n:
        if is_prime(i):
            count += 1
            prime = i
        i += 2

    return prime

if __name__ == "__main__":
    print(get_prime_number(10001))

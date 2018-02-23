#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 10:
# Find the sum of all the primes below two million.
def get_prime_numbers(n):
    """Gets all prime numbers below n."""
    primes, sieve = [], [True] * n

    for i in range(2, n):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                sieve[j] = False

    return primes

def get_prime_sum(n):
    """Calculate the sum of all prime numbers below n."""
    return sum(get_prime_numbers(n))

if __name__ == "__main__":
    print(get_prime_sum(2000000))

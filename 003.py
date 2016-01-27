#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 3:
# What is the largest prime factor of the number 600851475143 ?
def get_prime_factors(n):
    """Get all prime factors of n"""
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def get_largest_prime_factor(n):
    """Returns the largest prime factor of n"""
    return max(get_prime_factors(n))

if __name__ == "__main__":     
    print(get_largest_prime_factor(600851475143))

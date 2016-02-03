#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 4:
# Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(n):
    """Checks if n is a palindrome"""
    n = str(n)
    return n == n[::-1]

def get_largest_palindrome_product(max_number):
    """Returns the largest palindrome product."""
    largest_product = 0
    for i in range(max_number, 1, -1):
        if i * max_number <= largest_product:
            break;
        for j in range(max_number, i-1, -1):
            product = i*j
            if product <= largest_product:
                break;
            if is_palindrome(product):
                largest_product = product
    return largest_product

if __name__ == "__main__":
    print(get_largest_palindrome_product(9999))

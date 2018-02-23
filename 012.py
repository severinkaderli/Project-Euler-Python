#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# Project Euler - Problem 12:
# What is the value of the first triangle number to have over
# five hundred divisors?
import math

def get_triangle_number_with_n_factors(n):
	"""Return the value of the first triangle number with more than n factors."""
	for i in range(1, 1000000):
		triangle_number = get_triangle_number(i)
		number_of_factors = get_number_of_factors(triangle_number)
		if number_of_factors >= n:
			return triangle_number

def get_triangle_number(n):
	return ((n + 1) * n) // 2

def get_number_of_factors(n):
	number_of_factors = 0

	for i in range(1, int(math.sqrt(n)), 1):
		if n % i == 0:
			number_of_factors += 2

	return number_of_factors

if __name__ == "__main__":
	print(get_triangle_number_with_n_factors(500))

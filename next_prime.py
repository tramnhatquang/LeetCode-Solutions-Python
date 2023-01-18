from is_prime import is_prime


def next_prime(number: int) -> int:
	"""
	Given a number, return the next smallest prime number
	:param number:
	:type number:
	:return:
	:rtype:
	"""

	# 	Given a number, return the next smallest prime number
	# iterate from n + 1 to inf
	# if a curr number is prime, return this number
	# else, continue to increment and re-evaluate the next number
	# repeat until we find the next largest prime number, since it is guaranteed to exist

	# Given a number n, the largest factor of n is √n. This should imply, the loop to find if a number is prime should stop at √n.

	if number <= 1:
		return 2

	number += 1
	while True:
		if is_prime(number):
			return number
		number += 1


# time: O(sqrt(n)), space: O(1)


if __name__ == '__main__':
	assert next_prime(3) == 5
	assert next_prime(1) == 2
	assert next_prime(-10) == 2  # edge case

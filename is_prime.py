import math


def is_prime(number: int) -> bool:
	# a prime number can only be divisible 1 and itself
	# all numbers starting from 2 to n - 1 can not be divided
	if number < 2:
		return False
	if number < 4:
		return True

	for i in range(4, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False

	return True


# time: O(sqrt(number))
# space: O(1)

if __name__ == '__main__':
	assert is_prime(2) is True
	assert is_prime(-10) is False
	assert is_prime(0) is False
	assert is_prime(19) is True
	assert is_prime(100) is False

import math


def check_two_sum_primes(number: int) -> (int, int) or None:
	for num in range(2, number // 2 + 1):
		if is_prime(num) and is_prime(number - num):
			return num, number - num

	return None


def is_prime(number: int) -> bool:
	for i in range(2, int(math.sqrt(number) + 1)):
		if number % i == 0:
			return False

	return True


# time: O(sqrt(n))
# space: O(1)

if __name__ == '__main__':
	print(check_two_sum_primes(200))
	print(check_two_sum_primes(1000))

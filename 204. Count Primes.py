class Solution:
	def countPrimes_optimal(self, n: int) -> int:
		if n <= 2:
			return 0

		# Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
		# Initialze numbers[2] through numbers[n-1] as True because we assume each number
		# is prime until we find a prime number (p) that is a divisor of the number
		numbers = [False, False] + [True] * (n - 2)
		for p in range(2, int(sqrt(n)) + 1):
			if numbers[p]:
				# Set all multiples of p to false because they are not prime.
				for multiple in range(p * p, n, p):
					numbers[multiple] = False

		# numbers[index] will only be true where index is a prime number
		# return the number of indices whose value is true.
		return sum(numbers)

# time: O(sqrt(n) * log(log(n)))
# space: O(1)


def countPrimes_brute_force(self, n: int) -> int:
	def is_prime(number: int) -> bool:
		# check the curr number is is_prime
		for i in range(2, int(math.sqrt(number) + 1)):
			if number % i == 0:
				return False

		return True

	count = 0
	for i in range(2, n + 1):
		if is_prime(i):
			count += 1

	return count

# it leads to an TLE Solution
# think about the optimal one (sieve of Eratosthenes)

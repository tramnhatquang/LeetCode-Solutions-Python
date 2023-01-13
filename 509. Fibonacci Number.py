class Solution:
	def fib(self, N):
		# use memoization by storing the expensive calls into the hash map and retrieve it immediately if needed without re-calculating the calls
		cache = {}

		def recur_fib(N):
			if N in cache:
				return cache[N]

			if N < 2:
				result = N
			else:
				result = recur_fib(N - 1) + recur_fib(N - 2)

			# put result in cache for later reference.
			cache[N] = result
			return result

		return recur_fib(N)

	def fib_recursive_without_memoization(self, n: int) -> int:
		# n = 0 -> fib(0) = 0
		# n = 1 -> fib(1) = 1
		# f(n) = f(n -1 ) + f(n-2) if n > 1
		# use recursion without memoization
		# it costs TLE

		# establish the base cases
		if n < 2:
			return n

		return self.fib_recursive_without_memoization(n - 1) + self.fib_recursive_without_memoization(n - 2)

# time: O(2^n), space: O(n)

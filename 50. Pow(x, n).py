class Solution:

	def myPow_recursive(self, x: float, n: int) -> float:
		# observation: x^n = x*x*x*.....x where n is the numbers of x
		# we can take advantage of recursion here

		# note that n can be positive and negative
		# 2^(-3) = 1/(2^3)
		# convert n into a positive integer and take care of the sign later

		# base case
		if n == 0:
			return 1
		elif n < 0:  # handle when n < 0
			return 1 / self.myPow_recursive(x, -n)

		return x * self.myPow_recursive(x, n - 1)

	# time: O(2^n) -> causes maximum recursion depth exceeded -> think about the iterative way to reduce the time and space complexity

	def myPow_built_in_solution(self, x: float, n: int) -> float:
		# using the built-in method
		# not very useful in an interview
		return math.pow(x, n)  # or we can use x ** na

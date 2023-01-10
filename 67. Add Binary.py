class Solution:
	def addBinary(self, a, b) -> str:
		# Brute force solution
		# 1. Convert each binary string to numbers
		# 2. Add them up and convert the sum back to its binary string form
		# 3. Return the binary string
		# NOTE THAT: int(x, f) where x is the number in the form f
		# f could be binary (2), decimal (10), octal (8), etc

		return bin(int(a, 2) + int(b, 2))[2:]

	# time: O(n + m), space: O(max(n, m))

	def addBinary_optimal(self, a, b) -> str:
		# Using Bit manipulation

		x, y = int(a, 2), int(b, 2)
		while y:
			x, y = x ^ y, (x & y) << 1
		return bin(x)[2:]

# time: O(n + m ), where n, m are length of two strings respectively
# space: O(max(n + m))

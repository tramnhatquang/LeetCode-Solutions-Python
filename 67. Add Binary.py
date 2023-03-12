class Solution:

	def addBinary_no_built_in(self, a: str, b: str) -> str:
		res = ""
		carry = 0

		# adding from the end
		a, b = a[::-1], b[::-1]

		for i in range(max(len(a), len(b))):
			digitA = ord(a[i]) - ord("0") if i < len(a) else 0
			digitB = ord(b[i]) - ord("0") if i < len(b) else 0

			total = digitA + digitB + carry
			char = str(total % 2)
			res = char + res
			carry = total // 2

		if carry:
			res = "1" + res
		return res

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
		# 1. Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.
		# 2. while carry (y != 0)
		# 	- Current answer without carry is XOR of x and y: answer =x^y
		# 	- Current carry is left-shifted AND of x and y: carry = (x & y) << 1
		# - Job is done, prepare the next loop, x = answer, y = carry
		# 3. Return x in the binary form

		x, y = int(a, 2), int(b, 2)
		while y:
			x, y = x ^ y, (x & y) << 1

		# x^y computes the sum without carry
		# (x & y) << 1 computes the carry
		return bin(x)[2:]
# time: O(n + m ), where n, m are length of two strings respectively
# space: O(max(n + m))

class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		# Approach 1: we convert each string to int and add them up together. After that, we convert the result back to string type
		# time: O(n + m) where n, m is the length of num1, num2
		# space: O(1)
		# return str(int(num1) + int(num2))

		# Approach 2: Using an elementary math by adding two numbers step by step from least significant digit to the most significant digit. We use an extra variable 'carry' to carry the addition to the next digits
		p1, p2 = len(num1) - 1, len(num2) - 1
		res = []
		carry = 0
		while p1 >= 0 or p2 >= 0 or carry:
			if p1 >= 0:
				carry += ord(num1[p1]) - ord('0')
				p1 -= 1
			if p2 >= 0:
				carry += ord(num2[p2]) - ord('0')
				p2 -= 1
			res.append(carry % 10)
			carry //= 10

		return ''.join(str(x) for x in res[::-1])

	# time: O(max(n, m)) where n, m are lengths of num1, num2
	# space: O(max(n, m))

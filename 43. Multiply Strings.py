class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		# approach 1: Use the built in int() function to covert these strings into numbers, find the multiplication and then conver the result back to string

		# Not acceptable and it conflicts with the requirements
		# time: O(N * M) where N,M are lengths of num1, num2 respectively
		# return str(int(num1) * int(num2))

		# approach 2: Convert each string into the number and conver the result back into string
		if num1 == '0' or num2 == '0':
			return '0'

		def decode(num: str) -> int:
			ans = 0
			for i in num:
				ans = ans * 10 + (ord(i) - ord('0'))
			return ans

		def encode(num: int) -> str:
			res = ''
			while num:
				least_digit = num % 10
				num //= 10
				res = chr(ord('0') + least_digit) + res

			return res

		return encode(decode(num1) * decode(num2))

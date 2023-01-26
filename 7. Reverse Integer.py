class Solution:
	def reverse(self, x: int) -> int:
		# Build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow

		# Python does not have MIN, MAX values, so we have to find it
		MAX = 2 ** 31 - 1  # 2147483647
		MIN = -2 ** 31  # -2147483648

		print(MAX, MIN)
		sign = 1
		if x < 0:
			sign = -1
			x = -x

		reversed = 0
		while x:
			last_digit = x % 10
			x //= 10

			# check if reversed number is out of bound
			if (reversed > MAX / 10) or (reversed == MAX and last_digit > 7):
				return 0
			if (reversed < MIN / 10) or (reversed == MIN and last_digit < -8):
				return 0
			reversed = reversed * 10 + last_digit
		return reversed * sign

# time: O(log n)
# space: O(1)

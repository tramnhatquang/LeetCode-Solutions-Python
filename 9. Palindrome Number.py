class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		elif 0 <= x < 10:
			return True

		reversedX = 0
		num = x
		while num:
			reversedX = reversedX * 10 + num % 10
			num //= 10

		return x == reversedX

	# time: O(n)
	# reverse the given number. Since Python does not have an upper bound for
	# number, we do not care much about the overflow

	def isPalindrome_1(self, x: int) -> bool:
		if x < 0:
			return False
		elif 0 <= x < 10:
			return True
		elif x % 10 == 0:
			return False

		reversedX = 0
		while x > reversedX:
			reversedX = reversedX * 10 + x % 10
			x //= 10

		return x == reversedX or x == reversedX // 10
# time: O(n), space: O(1)

# we reverse half of the given number to avoid overflow
# 1. If the number of digits is odd, check x == reversedX // 10
# 2. If the number of digits is even, check x == reversedX

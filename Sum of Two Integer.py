class Solution:
	def getSum(self, a: int, b: int) -> int:
		# since Python has no 32-bits limit, its negative integer is entriely different
		# bitmask = mask = 0xFFFFFFFF

		mask = 0xFFFFFFFF

		while b != 0:
			a, b = (a ^ b) & mask, ((a & b) << 1) & mask

		max_int = 0x7FFFFFFF
		return a if a < max_int else ~(a ^ mask)

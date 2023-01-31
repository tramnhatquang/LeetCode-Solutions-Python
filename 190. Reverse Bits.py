class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		ret, power = 0, 31
		while n:
			ret += (n & 1) << power
			n = n >> 1
			power -= 1
		return ret

# time: O(1), since we only deal with 32 unsigned integer
# space: O(1)

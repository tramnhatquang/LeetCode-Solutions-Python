class Solution:

	def hammingWeight_optimal(self, n: int) -> int:
		"""
		Optimal solution
		"""
		count = 0
		while n:
			count += 1
			n = n & (n - 1)  # since n & (n- 1) will remove the least significant 1-bit in n to 0, and keeps all
		# other bits the same
		return count

	# time = space = O(1)

	def hammingWeight_optimal_2(self, n: int) -> int:
		# traverse and count the 1
		ans = 0
		while n > 0:
			if n & 1:  # check if the least significant digit is 1
				ans += 1
			print('Before: ', n)
			n >>= 1  # shift to the right
		return ans

	# time: O(1) = space since we are given 32-bit unsigned integer

	def hammingWeight(self, n: int) -> int:
		"""
		1. Convert the number to binary string
		2. Traverse thr the binary string and count numbers of 1s
		3. Return count
		"""
		return bin(n)[2:].count('1')


# time: O(1), space: O(1)


if __name__ == '__main__':
	a = 12
	print(type(bin(12)))
	print(bin(12))

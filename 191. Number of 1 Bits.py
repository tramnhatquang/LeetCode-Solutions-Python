class Solution:
	def hammingWeight(self, n: int) -> int:
		"""
		1. Convert the number to binary string
		2. Traverse thr the binary string and count numbers of 1s
		3. Return count
		"""
		binary_string = bin(n)
		count = 0
		for digit in binary_string:
			if digit == '1':
				count += 1
		return count

	# time: O(n), space: O(1)

	def hammingWeight_optimal(self, n: int) -> int:
		"""
		Optimal solution
		"""
		count = 0
		while n:
			count += 1
			n = n & (n - 1)
		return count


if __name__ == '__main__':
	a = 12
	print(type(bin(12)))
	print(bin(12))

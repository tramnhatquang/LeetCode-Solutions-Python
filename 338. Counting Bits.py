from typing import *


class Solution:

	def countBits_optimal(self, n: int) -> List[int]:
		# there is an observation that
		# if n is even, the number of ones in binary string of n is equal to number of ones in n /2
		# if n is odd, the number of ones in binary string of n is equal to number of ones in n/2 + 1
		res = [0] * (n + 1)
		for i in range(1, len(res)):
			if i % 2:  # odd
				res[i] = res[i // 2] + 1
			else:
				res[i] = res[i // 2]

		return res

	# time: O(n), space: O(1)

	def countBits(self, n: int) -> List[int]:

		# make an arraay of size (n + 1)
		# for each number from 0 to n + 1:
		#   - COunt the number of 1s in each number

		def count_1_bits(number: int) -> int:
			count = 0
			while number:
				number &= number - 1
				count += 1
			return count

		# time: O(log(number)) (log_2 exactly)
		# space: O(1)

		res = [0] * (n + 1)
		for i in range(len(res)):
			res[i] = count_1_bits(i)
		return res

	# time: O(n log n)
	# space: O(1), if we ignore the output arr

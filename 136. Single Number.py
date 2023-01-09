import collections
from typing import *


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		# BRUTE FORCE Solution
		# 1. Use a hash map to count the frequencies of each singleNumber
		# 2. Return the number whose frequency is equal to 1
		counter = collections.Counter(nums)

		for num in counter:
			if counter[num] == 1:
				return num

	# time = space = O(n)

	def singleNumber_optimal(self, nums: List[int]) -> int:
		# Optimal solution
		# 1. If we take XOR of zero and some bit, it will return that bit
		# a ^ 0 = a
		# 2. If we take XOR of two same bits, it will return 0
		# a ^  a = 0
		# Then a ^ b ^ a = (a  ^ a) ^ b = 0 ^ b = b
		res = 0
		for i in nums:
			res ^= i
		return res
	# time: O(n), space: O(1)

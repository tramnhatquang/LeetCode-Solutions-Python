from typing import *


class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		# BRUTE FORCE Solution

		# 1. Converting the given arr to a set to increase the look-up time O(1) in Python
		# 2. Traverse through 0 to n inclusively and find out the number that is not in the num_set. That's our missing number
		num_set = set(nums)

		for num in range(len(nums) + 1):
			if num not in num_set:
				return num

	# time: O(n) = space, n is the length of arr
	# space is O(n) since we use a new set to contain all elements from nums

	def missingNumber_optimal(self, nums: List[int]) -> int:
		# OPTIMAL solution

		# Using Gauss's formula
		# sum of numbers starting from 0 to n is n(n + 1) / 2
		n = len(nums)
		total_sum = n * (n + 1) // 2
		return total_sum - sum(nums)
	# time: O(n), space = O(1)

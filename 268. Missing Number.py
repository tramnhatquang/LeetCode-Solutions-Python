from typing import *


class Solution:
	def missingNumber_cyclic_sort(self, nums: List[int]) -> int:
		# using cyclic sort to solve this problem
		i = 0
		n = len(nums)
		while i < n:
			curr_value = nums[i]
			if i != curr_value:
				# swap, put curr value at its correct index
				# check the case when the curr_val = len(arr)
				if curr_value == n:
					i += 1
				else:
					# swap
					nums[curr_value], nums[i] = nums[i], nums[curr_value]
			else:
				i += 1

		print(f'Nums arr: {nums}')
		for i in range(n):
			if i != nums[i]:
				return i
		# all the numbers are placed correctly at their indices
		return n  # the missing number is the length

	def missingNumber_using_xor(self, nums):
		missing = len(nums)
		for i, num in enumerate(nums):
			missing ^= i ^ num
		return missing

	def missingNumber_optimal(self, nums: List[int]) -> int:
		# OPTIMAL solution

		# Using Gauss's formula
		# sum of numbers starting from 0 to n is n(n + 1) / 2
		n = len(nums)
		total_sum = n * (n + 1) // 2
		return total_sum - sum(nums)

	def missingNumber(self, nums: List[int]) -> int:
		# BRUTE FORCE Solution

		# 1. Converting the given arr to a set to increase the look-up time O(1) in Python
		# 2. Traverse through 0 to n inclusively and find out the number that is not in the num_set. That's our missing number
		num_set = set(nums)

		for num in range(len(nums) + 1):
			if num not in num_set:
				return num

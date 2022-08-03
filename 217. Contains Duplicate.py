from typing import List


class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		# approach 1: Hash Set
		# For each iteration, check if a number is already on the set. Otherwise, add that number to the set. Returns true if finding a duplicate number.
		nums_set = set()
		for num in nums:
			if num in nums_set:
				return True
			nums_set.add(num)
		return False

	# time = space = O(n), n is the length of nums
	# in the worst case, set contains up to n distinct characters

	# approach 2: Using built-in function
	# return len(nums) != len(set(nums))

	# approach 3: Sorting
	# 1. Sorting the nums
	# 2. After sorting, similar numbers are placed consecutively. For each iteration, we check if the number at (i + 1)-th is equal to number at i-th index
	#
	# nums.sort()
	# for i in range(len(nums) - 1):
	# 	if nums[i] == nums[i + 1]:
	# 		return True
	#
	# return False

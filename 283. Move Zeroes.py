from typing import List


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# Approach 1: Use a two pointer technique
		# the left pointer points at the first index, and the right pointers is responsible to go through each index
		# if nums[right] is not zero, we swap nums[left] and nums[right] and advance left by 1
		# eventually, we get all Os to the end of the arr
		left = 0
		for right in range(len(nums)):
			if nums[right] != 0:
				nums[left], nums[right] = nums[right], nums[left]
				left += 1

	# time: O(n), space: O(1), n is the length of nums

from typing import *


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		inserted_index = 0
		n = len(nums)

		for i in range(n):
			if nums[i] != val:
				# swap
				nums[i], nums[inserted_index] = nums[inserted_index], nums[i]
				inserted_index += 1

		return inserted_index

	# Time: O(n), space: O(1), where n is the length of nums
	# However, if the replaced number is rare, we make unnecessary copies
	# For example, if arr = [1, 2, 3, 4, 5], targetVal = 5
	# We make 4 unnecessary copies for number 1, 2, 3, 4
	# Another approach is introduced in the second Solution

	def removeElement_1(self, nums: List[int], val: int) -> int:
		n = len(nums)

		i = 0
		while i < n:
			if nums[i] == val:
				nums[i] = nums[n - 1]
				# reduce the arr size by 1
				n -= 1
			else:
				i += 1

		return n

	# time: O(n), space: O(1)

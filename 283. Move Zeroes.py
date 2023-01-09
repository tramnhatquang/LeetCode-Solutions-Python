class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# use two pointers
		# left pointer points at the new index to insert non-zero value
		# right pointer traverses thr each index in the arr
		# 1. When the right pointer points at a non-zero element, swap the elements between left and right pointer. Then increment the left pointer by 1
		# 2. Keep increasing the right pointer until it completely traverses thr the arr. The result will have all zeroes moved to the end

		left = 0
		for right in range(len(nums)):
			if nums[right] != 0:
				nums[left], nums[right] = nums[right], nums[left]
				left += 1

		# time: O(n), space: O(1), n is length of arr

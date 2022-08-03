from typing import List


class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		# approach 1: Using an extra array to store each value from nums with
		# the new indices. The new index is placed at the index (i + k) %
		# nums.length. Then we copy the new array to the original one n = len(
		# nums) res = [None] * n for i in range(n): res[(i + k) % n] = nums[i]
		# nums[:] = res

		# time = space =  O(n), n is the length of nums

		# approach 2: Rotate in-place using a helper function reverse
		# notice that given arr [1, 2, 3, 4, 5] , k = 3
		# new arr = [3, 4, 5, 1, 2] = res
		# If we reverse the whole arr, arr = [5, 4, 3, 2, 1]
		# if we reverse the first k numbers, arr = [3, 4, 5, 2, 1]
		# if we reverse the last n - k numbers, arr = [3, 4, 5, 1, 2]
		def reverse(left: int, right: int) -> None:
			"""
			Swapping the arr in-place from left index to right index (inclusive)
			"""
			while left < right:
				nums[left], nums[right] = nums[right], nums[left]
				left += 1
				right -= 1

		n = len(nums)
		k %= n
		# reverse the whole arr
		reverse(0, n - 1)

		# reverse the first k numbers
		reverse(0, k - 1)

		# reverse the last n - k numbers
		reverse(k, n - 1)

# time: O(n), space: O(1)

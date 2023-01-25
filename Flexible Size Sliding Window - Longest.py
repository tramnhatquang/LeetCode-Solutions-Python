from typing import List

"""
Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).
"""


def subarray_sum_longest(nums: List[int], target: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	left = res = 0
	n = len(nums)
	curr_sum = 0
	for right in range(n):
		curr_sum += nums[right]

		# shrink the window if sum of window exceeds target
		while curr_sum > target:
			curr_sum -= nums[left]
			left += 1
		res = max(res, right - left + 1)
	return res
# time: O(n), space: O(1)

from typing import List

"""
Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.
"""


def subarray_sum_fixed(nums: List[int], k: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE

	n = len(nums)
	if n < k:
		return -1
	curr_max = 0
	# processing the first k elements
	# use sliding window to solve the problem, whenever the window size > k, remove the leftmost element and add the rightmost element
	# record the global max so far
	for i in range(k):
		curr_max += nums[i]

	global_max = curr_max
	for right in range(k, n):
		left = right - k
		curr_max -= nums[left]
		curr_max += nums[right]
		global_max = max(global_max, curr_max)
	return global_max

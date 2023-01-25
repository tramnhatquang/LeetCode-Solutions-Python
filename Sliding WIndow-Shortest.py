from typing import List


def subarray_sum_shortest(nums: List[int], target: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	curr_sum = left = 0
	length = len(nums)

	for right in range(len(nums)):
		curr_sum += nums[right]
		while curr_sum >= target:  # shrink the window whenever the curr sum >= target
			length = min(length, right - left + 1)
			curr_sum -= nums[left]
			left += 1

	return length

# time: O(n), space: O(n)

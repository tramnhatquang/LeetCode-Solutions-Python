from typing import *


class Solution:

	# BRUTE FORCE SOLTUION
	# 1. TRY EVERY POSSIBLE SEQUENCE
	# 2. COUNT NUMBER OF ZEROES IN EACH SEQUENCE
	# 3. If our sequence has one or fewer 0's, check if that's the longest consecutive sequence of 1's.
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		longest_sequence = 0
		for left in range(len(nums)):
			num_zeroes = 0

			for right in range(left, len(nums)):
				if num_zeroes == 2:
					break
				if nums[right] == 0:
					num_zeroes += 1
				if num_zeroes <= 1:
					longest_sequence = max(longest_sequence, right - left + 1)

		return longest_sequence

	# MORE OPTIMAL SOLUTION

	def findMaxConsecutiveOnes_optimal(self, nums: List[int]) -> int:
		longest_sequence = 0
		left, right = 0, 0
		num_zeroes = 0

		while right < len(nums):  # while our window is in bounds
			if nums[right] == 0:  # add the right most element into our window
				num_zeroes += 1

			while num_zeroes == 2:  # if our window is invalid, contract our window
				if nums[left] == 0:
					num_zeroes -= 1
				left += 1

			longest_sequence = max(longest_sequence,
								   right - left + 1)  # update our longest sequence answer
			right += 1  # expand our window

		return longest_sequence
# time: O(n)
# space: O(1)

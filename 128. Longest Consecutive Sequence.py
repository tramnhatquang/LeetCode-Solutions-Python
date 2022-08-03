from typing import *


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		# 1. sort the array first
		# 2. keep the longest_count and curr count so far
		# 3. Similar elements are adjacent to each other in the sorted order, so we can skip them. If the next element is consecutive to the curr element, increment the curr count
		# 4. If not, we update the longest_count so far and reset the curr count to 1

		#         if not nums:
		#             return 0
		#         nums.sort()
		#         longest_count = curr_count = 1
		#         for i in range(1, len(nums)):
		#             if nums[i] != nums[i - 1]:
		#                 if nums[i] == nums[i - 1] + 1:
		#                     curr_count += 1
		#                 else:
		#                     longest_count = max(longest_count, curr_count)
		#                     curr_count = 1

		#         return max(longest_count, curr_count)

		# time = O(n log n), space: O(1), n is the length of input

		# Using hash set with optimization 1. hash set the original list 2. we
		# only build the sequence from the start, which means the precede
		# number does not belong to the set.
		if not nums:
			return 0
		longest_count = 1
		num_set = set(nums)

		for num in num_set:
			if num - 1 not in num_set:
				curr_count = 1

				while num + 1 in num_set:
					num += 1
					curr_count += 1

				longest_count = max(longest_count, curr_count)
		return longest_count

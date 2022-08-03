from collections import *
from typing import *


class Solution:
	def countKDifference(self, nums: List[int], k: int) -> int:
		# approach 1: Brute-force solution
		# 1. Find all the absolute diffs of every possible pairs. If the different is equal to the target, increment the count
		# time: O(n^2), space: O(1)

		# count = 0
		# for i in range(len(nums) - 1):
		#     for j in range(i + 1, len(nums)):
		#         if abs(nums[j] - nums[i]) == k:
		#             count += 1
		# return count

		# approach 2: Hash table, two passses
		# We count the number of times each number shows up in the array, then for each number, we check if it + k is in the dict.
		# If it is, then we generated # of pairs equal to the number of times val + k showed up.
		# e.g., for [2, 2, 1, 1], when num = 1, we have two 2s, so we add 2 pairs. when num = 1 again, we add another 2 pairs.
		# We don't need to check if it - k is in the array because that value has already incremented counter in another part of the array.
		#         nums_dict, count = {}, 0
		#         for num in nums:
		#             if num not in nums_dict:
		#                 nums_dict[num] = 1
		#             else:
		#                 nums_dict[num] += 1

		#         for num in nums:
		#             if num + k in nums_dict:
		#                 count += nums_dict[num + k]
		#         return count

		# time: O(n), space: O(n)

		# approach 3: Hash table, one-pass
		seen = defaultdict(int)
		counter = 0
		for num in nums:
			counter += seen[num - k] + seen[num + k]
			seen[num] += 1
		return counter

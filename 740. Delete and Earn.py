import collections
from typing import List


class Solution:
	def deleteAndEarn_bottom_up_optimal(self, nums: List[int]) -> int:
		points = collections.defaultdict(int)
		max_number = max(nums)
		# Precompute how many points we gain from taking an element
		for num in nums:
			points[num] += num

		# Base cases
		two_back = 0
		one_back = points.get(1, 0)

		for num in range(2, max_number + 1):
			two_back, one_back = one_back, max(one_back, two_back + points.get(num, 0))

		return one_back


# time: O(N + k), N is length of nums, k is the max number
# space: O(N) for the hash table's space


def deleteAndEarn_top_down(self, nums: List[int]) -> int:
	points = collections.defaultdict(int)
	max_number = max(nums)
	for num in nums:
		points[num] += num

	def max_points(num: int) -> int:
		if num == 0:  # 0 points
			return 0
		elif num == 1:
			return points[1]

		# apply recurrence relation
		return max(max_points(num - 1), max_points(num - 2) + points[num])

	return max_points(max_number)

# time: O(N + k), N is length of nums, k is the max element in nums
# space: O(N + k) -> This approach causes TLE

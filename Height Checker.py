import collections
from typing import *


class Solution:
	def heightChecker(self, heights: List[int]) -> int:
		sorted_arr = list(sorted(heights))

		count = 0
		for i in range(len(heights)):
			if heights[i] != sorted_arr[i]:
				count += 1

		return count

	# time: O(n log n)
	# space: O(n)

	# Basically, I sort the given arr and compare each num in the sorted and
	# original arr. I use a count variable to count each different number and
	# then return the count

	# a better solution

	def heightChecker_optimal(self, heights: List[int]) -> int:
		cnt = collections.Counter(heights)
		i, ans = 1, 0
		for h in heights:
			while cnt[i] == 0:  # non-exist height.
				i += 1  # skip it.
			if i != h:  # mismatch found.
				ans += 1  # increase by 1.
			cnt[i] -= 1  # remove the one that has been used.
		return ans


if __name__ == '__main__':
	s = Solution()
	assert s.heightChecker_optimal([1, 1, 4, 2, 3]) == 3

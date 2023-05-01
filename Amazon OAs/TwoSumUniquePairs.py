from typing import *


class Solution:

	def two_sum_unique_pairs(self, nums: List[int], target: int) -> int:
		"""
		Return the number of unique pairs that add up to target
		"""
		seen = set()  # denotes the number of seen, unique pairs we have seen so far
		complement = set()  # denotes the numbers we seen so far
		for num in nums:
			if target - num in complement:
				pair = (num, target - num) if num < target - num else (target - num, num)
				seen.add(pair)
			complement.add(num)
		return len(seen)

# time: O(n)
# space: O(2n) = O(n), n is the length of nums


if __name__ == '__main__':
	s = Solution()
	assert s.two_sum_unique_pairs([1, 5, 1, 5], 6) == 1
	assert s.two_sum_unique_pairs([1, 1, 2, 45, 46, 46], 47) == 2
	assert s.two_sum_unique_pairs([1, 1], 2) == 1

from typing import List


class Solution:
	def minIncrementForUnique(self, nums: List[int]) -> int:
		"""
		- Sort the input arr
		- The curr number must be at least the (prev + 1) to make the arr uniquely
		TC: O(n log n), n is length of arr
		SC: O(n)
		"""
		if not nums:
			return 0
		nums.sort()
		min_increment = 0
		next_val = nums[0]
		for num in nums:
			if num < next_val:
				min_increment += next_val - num
				next_val += 1
			else:
				next_val = num + 1
		return min_increment


if __name__ == '__main__':
	s = Solution()
	s.minIncrementForUnique([1, 1, 1])
	s.minIncrementForUnique([4, 1, 3, 2, 2])

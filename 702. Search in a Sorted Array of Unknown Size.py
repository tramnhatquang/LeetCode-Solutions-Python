# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
	def search(self, reader: 'ArrayReader', target: int) -> int:
		"""
		- Brute force algo: call interface into each index in the hidden arr -> find the target or not. Time: O(n)
		- Use Binary Search to solve this problem
			+ The first subproblem: Find the search limit or the upper bound of the binary Search
			+ Perfom the bianry search in the defined boundaries
		"""
		if reader.get(0) == target:
			return 0
		MAX_BOUND = 2 ** 31 - 1

		right = 1
		while reader.get(right) < target and reader.get(right) != MAX_BOUND:
			right *= 2

		left = right // 2
		while left <= right:
			mid = (left + right) // 2
			val = reader.get(mid)

			if val == target:
				return mid
			elif val > target:
				right = mid - 1
			else:
				left = mid + 1
		return -1

# time: O(log n + log n ) = O(log n). It takes O(log n) to find the upper bound and also O(log n) to do the binary search

# space: O(1)

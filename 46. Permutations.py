from typing import *


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		res = []

		def backtrack(arr=[]) -> None:
			# base case
			if len(arr) == len(nums):
				res.append(arr[:])
				return

			for num in nums:
				if num not in arr:
					arr.append(num)
					backtrack(arr)
					arr.pop()

		backtrack()
		return res

	# time: O(n * n!) for permutation formula
	# space: O(n!)


if __name__ == '__main__':
	s = Solution()
	print(s.permute([1, 2, 3]))

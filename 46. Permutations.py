from typing import *


class Solution:
	def permute_1(self, nums: List[int]) -> List[List[int]]:
		# use a
		res = []

		def backtrack(path: List[int], used: List[bool]) -> None:
			# base case
			if len(path) == len(nums):
				res.append(path.copy())
				return

			for index, number in enumerate(nums):
				# check if number is not visited
				if not used[index]:
					path.append(number)
					used[index] = True
					backtrack(path, used)
					# remove letter from permutation, mark letter as unused
					path.pop()
					used[index] = False

		backtrack([], [False] * len(nums))
		return res

	def permute_2(self, nums: List[int]) -> List[List[int]]:
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
	print(s.permute_1([1, 2, 3]))

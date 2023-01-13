class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		res = []

		def backtrack(arr, index) -> None:
			if index > len(nums):
				return

			# make a shallow copy
			res.append(arr[:])

			for j in range(index, len(nums)):
				arr.append(nums[j])
				backtrack(arr, j + 1)
				arr.pop()

		backtrack([], 0)
		return res

# time: O(n * 2^n) n is the length of arr
# spacE: O(n)

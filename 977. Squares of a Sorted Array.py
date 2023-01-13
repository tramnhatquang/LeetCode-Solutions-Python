from typing import List


class Solution:
	def sortedSquares_two_pointer_1(self, nums: List[int]) -> List[int]:
		# using two pointers but with clear code
		res = [0] * len(nums)
		left, right = 0, len(nums) - 1

		while left <= right:
			left_num, right_num = abs(nums[left]), abs(nums[right])
			if left_num < right_num:
				res[right - left] = right_num ** 2
				right -= 1
			else:
				res[right - left] = left_num ** 2
				left += 1

		return res

	# time: O(n), one pass using two pointer
	# space: O(1),output array is not considered for space complexity.

	def sortedSquares_two_pointer_2(self, nums: List[int]) -> List[int]:
		# Use the two pointer technique, because we are given a sorted arr
		res = [None] * len(nums)
		inserted_index = len(nums) - 1

		left, right = 0, len(nums) - 1
		while left <= right:
			left_square = nums[left] ** 2
			right_square = nums[right] ** 2
			if left_square < right_square:
				res[inserted_index] = right_square
				right -= 1
			else:
				res[inserted_index] = left_square
				left += 1
			inserted_index -= 1

		return res

	# time: O(n), n: length of nums
	# space: O(1)

	def sortedSquares_brute_force(self, nums: List[int]) -> List[int]:
		# brute force Solution
		# square its number in the arr and sort them after all

		# time: O(n log n), n: length of nums
		# space: O(n)

		nums = [x ** 2 for x in nums]
		nums.sort()
		return nums

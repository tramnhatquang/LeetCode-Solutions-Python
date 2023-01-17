from typing import List


class Solution:

	def sortColors_one_pass(self, nums: List[int]) -> None:

		# The problem is knows as Dutch National Flag Problem and first was proposed by Edsger W. Dijkstra. The idea
		# is to attribute a color to each number and then to arrange them following the order of colors on the Dutch flag
		"""
		      Dutch National Flag problem solution.
		"""
		# for all idx < p0 : nums[idx < p0] = 0
		# curr is an index of element under consideration
		p0 = curr = 0
		# for all idx > p2 : nums[idx > p2] = 2
		p2 = len(nums) - 1

		while curr <= p2:
			if nums[curr] == 0:
				nums[p0], nums[curr] = nums[curr], nums[p0]
				p0 += 1
				curr += 1
			elif nums[curr] == 2:
				nums[curr], nums[p2] = nums[p2], nums[curr]
				p2 -= 1
			else:
				curr += 1

	def sortColors_two_passes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# the two-pass Solution
		# 1. count the occurrences of 1s, 2s, and 0s
		# 2. Overwrite array with the total number of 0's, then 1's and followed by 2's.
		zeroes = ones = twos = 0
		for element in nums:
			if element == 0:
				zeroes += 1
			elif element == 1:
				ones += 1
			elif element == 2:
				twos += 1
		for i in range(len(nums)):
			if zeroes > 0:
				nums[i] = 0
				zeroes -= 1
			elif ones > 0:
				nums[i] = 1
				ones -= 1
			elif twos > 0:
				nums[i] = 2
				twos -= 1

	# time: O(n), space: O(1)
	def sortColors_sort(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		# easy approach is to sort the whole arr
		nums.sort()
# time: O(n log n), space: O(n)

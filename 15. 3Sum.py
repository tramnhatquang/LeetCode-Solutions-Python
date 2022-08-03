from typing import *


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		# Approach 1: brute force solution - Use three nested loop to find
		# three numbers adding up to the target - The first loop runs from (
		# i-indexed to (len(nums) -3 + 1)). The second inner loop runs from j
		# = (i + 1)-indexed to the end. The inner-most loop runs from (j +
		# 1)-indexed to the end time: O(n^3), space: o(1) which is inefficient

		# approach 2: Two pointers technique 1. Sort the array first 2. For
		# each number in the sorted array, fixed that number1, and find (
		# number2 + number3) == -(number1) in the remaining elements. Starting
		# the second number from the next index of number1 (index of number1
		# is i-indexed, index of number2 is (i+1)-indexed). The index of third
		# number starts from the last index in the arr. Advance left or right
		# pointers based on the total sum For similar numbers in the same arr,
		# we move on to the next number to skip duplicates

		nums.sort()
		triplets = []
		for index, num in enumerate(nums):
			if index > 0 and num == nums[index - 1]:
				continue

			# setting the left, right pointers
			left, right = index + 1, len(nums) - 1
			while left < right:
				total = num + nums[left] + nums[right]
				if total == 0:
					triplets.append([num, nums[left], nums[right]])
					left += 1
					right -= 1
					while left < right and nums[left] == nums[left - 1]:
						left += 1
					while left < right and nums[right] == nums[right + 1]:
						right -= 1
				elif total > 0:
					right -= 1
				else:
					left += 1

		return triplets

# time: O(n^2), space: O(1), n is the length of the input

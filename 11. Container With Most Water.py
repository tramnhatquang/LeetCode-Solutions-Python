from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		# approach 1: brute-force solution
		# compute the contained water between every pair of lines in the input
		# if not height:
		#     return 0
		# max_volume = 0
		# for col1 in range(len(height)):
		#     for col2 in range(col1, len(height)):
		#         width = col2 - col1
		#         max_volume = max(max_volume, min(height[col2], height[col1]) * width)
		# return max_volume

		# time: O(N^2), N IS THE LENGTH OF INPUT
		# SPACe: O(1)

		# approach 2: two pointers
		# the water contained between two vertical lines is determined by the height * width
		# height of water is determined by the min height of two lines
		# width is the diff between their indices
		#
		# If we use two pointers, one pointing at the first index, second one is pointing at the last index. if the height of the first on is lesser than the height of the second one, we move the left pointer ahead and compute the contained water. Update the max contained water if possible.

		# WHY DO WE MOVE THE LESSER HEIGHT POINTER BUT NOT THE HIGHER ONE?
		# AS WE MOVE TOWARD INSIDE, THE WIDTH IS DECREASING DUE TO DIFF BETWEEN TWO LINES AND THE HEIGHT IS DETERMINED BY THE MIN HEIGHT. IF WE MOVE THE HIGHER HEIGHT POINTER, WE REDUCE THE MAX WATER. BUT IF WE MOVE THE LESSER HEIGHT, WE MAY OBTAIN A BETTER MAX VOLUME, SINCE THE NEXT HEIGHT MAYBE HIGHER OR EQUAL TO THE THE SECOND ONE'S

		if not height:
			return 0
		left, right = 0, len(height) - 1
		max_volume = 0
		while left < right:
			curr_width = right - left
			max_volume = max(max_volume,
			                 min(height[left], height[right]) * curr_width)
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1

		return max_volume

# TIME: o(n), n is the length of input
# spacE: O(1)

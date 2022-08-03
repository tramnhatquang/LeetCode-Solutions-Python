from typing import List


class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		# using the two pointers technique to swap the string in-place
		left, right = 0, len(s) - 1
		while left < right:
			s[left], s[right] = s[right], s[left]
			left += 1
			right -= 1

	# time: O(n), space: O(1), where n is the length of s
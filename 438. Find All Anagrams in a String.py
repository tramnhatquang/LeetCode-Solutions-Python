from typing import *

from collections import Counter


class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:

		# Approach 1: Sliding window with Hash map
		# We use the collections.Counter to save some TC.
		if len(p) > len(s):
			return []

		# record the occurences of p
		counter_p = Counter(p)
		# record the occurences of s
		counter_s = Counter(s[:len(p)])

		res = [0] if counter_p == counter_s else []
		left = 0
		for right in range(len(p), len(s)):
			# append the rightmost character
			counter_s[s[right]] += 1

			# remove the leftmost character
			# shrinking the window, so that the length of the window is not larger than len(s)
			counter_s[s[left]] -= 1
			if counter_s[s[left]] == 0:
				counter_s.pop(s[left])

			left += 1
			if counter_s == counter_p:
				res.append(left)

		return res

	# time: O(N) where N is the length of s
	# spacE: O(k) where k is at most 26 lowercase letters. We can consider it is O(1) space

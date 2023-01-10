class Solution:
	def strStr(self, haystack: str, needle: str) -> int:

		# Brute force solution
		# 1. check every substring in the haystack and if we can get a match of a needle
		# 2. If we find our match, return the starting index.
		# 3. After the loop ends, return -1 if there is no match
		n = len(haystack)
		m = len(needle)

		if m > n:
			return -1

		for i in range(n - m + 1):
			if haystack[i:i + m] == needle:
				return i

		return -1

# time: O(mn) where m: length of haystack, n: length of needle
# space: O(n) length of needle from the substring

# NOTE THAT THE BETTER, OPTIMAL SOLUTION IS EITHER USE KMP ALGO OR
# BOOYER-MOORE ALGO
# LOOK IT UP IF NECESSARY

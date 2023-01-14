from collections import Counter


class Solution:
	def longestPalindrome(self, s: str) -> int:
		# 1. We count the occurrences of each character in the s
		# 2. Since we can use all the even-count characters for our longest palindrome.
		# However, we can possibly add a unique center character. For every
		# odd-count characters, we want to use up to (k - 1) occurrences of
		# these characters (k are the occurrences).  In the end, add 1 back to
		# the overall sum, since in palindrome, we can have one and only one
		# odd frequency character (highest out of all odd frequency
		# characters) and make the string longest palindrome.

		counter = Counter(s)
		longest_count = 0
		is_odd = False
		for key, val in counter.items():
			if val % 2 == 0:
				longest_count += val
			else:
				longest_count += val - 1
				is_odd = True

		if is_odd:
			return longest_count + 1
		return longest_count

# time: O(n)
# space: O(1) since we only use up to 26 lowercase letters

from collections import Counter
from typing import *


class Solution:
	def findAnagrams_arr(self, s: str, p: str) -> List[int]:
		# Sliding window to solve this problem
		# use two arr to count occurrences of p string and window string
		#   - Use size of 26 since we deal only with 26 lowercase letters
		#   - Whenever two arr are equal to each other, we found an anagram, and append the left index which indicates the starting index into the res arr

		s_len, p_len = len(s), len(p)
		if s_len < p_len:
			return []

		res = []
		p_counter = [0] * 26
		window_counter = [0] * 26

		# processing the first window
		for i in range(p_len):
			# get the ascii value and increase the occurrence
			p_counter[ord(p[i]) - ord('a')] += 1
			window_counter[ord(s[i]) - ord('a')] += 1

		if p_counter == window_counter:
			res.append(0)

		for i in range(p_len, s_len):
			# remove the leftmost element, which means removes the leftmost's occurrence from window counter
			window_counter[ord(s[i - p_len]) - ord('a')] -= 1
			window_counter[ord(s[i]) - ord('a')] += 1
			if window_counter == p_counter:
				res.append(i - p_len + 1)
		return res

	# space: O(N) where N is the length of S
	# time: O(26) = O(1), since we only deal with 26 lowercase English letters

	def findAnagrams_hash_map(self, s: str, p: str) -> List[int]:

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

a, b = "cbaebabacd", "ab"
s = Solution()
res = s.findAnagrams_hash_map(a, b)
print(res)

import collections
from typing import *


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		# approach 1: Categorize by Sorted String
		#   -Two strings are anagrams if and only if their sorted strings are equal.
		#   - use a map that has keys as sorted strings and vals as lists of strings that are the same after sorting and are equal to keys
		# Time: O(N KlogK) where N is the length of strs and K is the maximum length of a string in strs
		# Space: O(NK) the total information content stored in hash_table

		# hash_table = defaultdict(list)
		#
		# for string in strs:
		#     hash_table[tuple(sorted(string))].append(string)
		#
		# return hash_table.values()

		# approach 2: Categorize by Count
		# Counting the occurences of each character in a string and use them as a key in a dictionary
		# Time Complexity: O(N*K) where N is the length of the strs
		# K is the maximum length of a string in strs
		# Space: O(N*K), total information content stored in ans
		ans = collections.defaultdict(list)
		for string in strs:
			count = [0] * 26
			for char in string:
				count[ord(char) - ord('a')] += 1
			ans[tuple(count)].append(string)

		return list(ans.values())

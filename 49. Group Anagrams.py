import collections
from typing import *


class Solution:
	def groupAnagrams_count_chars(self, strs: List[str]) -> List[List[str]]:
		res = collections.defaultdict(list)  # each key has its value as a list

		for string in strs:
			# create a list of char's frequency in each string:
			count = [0] * 26  # since we only deal with lowercase letters
			for char in string:
				count[ord(char) - ord('a')] += 1

			# store the count list as a key in a map
			# we know two sorted strings are anagrams to each other
			# Python trick: key in map only allows immutable value
			res[tuple(count)].append(string)

		return list(res.values())

	# time: O(n * m) where n : length of strings, m is the longest length of string
	# space: O(n * m), total information content stored in res

	def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
		# approach 1: Categorize by Sorted String
		#   -Two strings are anagrams if and only if their sorted strings are equal.
		#   - use a map that has keys as sorted strings and vals as lists of strings that are the same after sorting and are equal to keys
		# Time: O(N KlogK) where N is the length of strs and K is the maximum length of a string in strs
		# Space: O(NK) the total information content stored in hash_table
		map = collections.defaultdict(list)

		for string in strs:
			map[tuple(sorted(string))].append(string)

		return list(map.values())


if __name__ == '__main__':
	a = collections.defaultdict(int)
	# b = collections.defaultdict(int)
	a[1] += 1
	a[2] += 1
	a[1] -= 1
	# b = {2: 1, 1: 0}
	c = {2: 1}
	print(a)
	print(c)
	assert a == c

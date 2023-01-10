class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		# VERTICAL SCANNING
		# 1. use the first string as our target
		# 2. Loop thr each char in the first string and check other strings if they contain that char at the same index. If they all satisfy, we continue scanning.
		# 3. Whenever a string does not contain a char, we know all the preceding chars are our longest common longestCommonPrefix
		# time: O(mn), m is the longest length of a string in strs, and n is the length of the arr. In some cases, we will have all same strings whose lengths are the same
		# space: O(n)
		# base case when the list is empty or none
		if strs is None or len(strs) == 0:
			return ""

		# for each character in first string
		for i in range(len(strs[0])):
			c = strs[0][i]
			# check if the other strings also have that character at same index
			for j in range(1, len(strs)):
				# if other strings are shorter or doesn't have the same character, stop
				if i == len(strs[j]) or strs[j][i] != c:
					return strs[0][:i]

		# return the complete first string as it's contained in all other at this point
		return strs[0]
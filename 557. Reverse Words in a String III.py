class Solution:
	def reverseWords(self, s: str) -> str:
		# Approach 1: Using a built-in function
		# time: O(n^2), space: O(n) where n is the length of the s
		# return ' '.join([word[::-1] for word in s.split()])

		# Approach 2: Without using a built-in function
		# 1. Using a two pointer technique. Left pointers points at the first
		# index, right pointer will move through each index. At any time,
		# if the s[right] == ' ', the range [left, right - 1] is the word we
		# need to reverse
		# 2. Define a function to reverse the range [left, right - 1] in
		# place. After that, move the left pointer to right + 1 - the start
		# of the next character (since each word is separated by a single
		# white space)
		# 3. Repeat step 1, 2 until we reach the end of the input
		res = ''
		start = 0
		end = 0
		while end < len(s):
			if s[end] == ' ':
				res += self.reverse_in_range(s, start, end - 1) + ' '
				start = end + 1
			end += 1

		return res + self.reverse_in_range(s, start, end - 1)

	def reverse_in_range(self, s, start, end):
		res = ''
		for i in reversed(range(start, end + 1)):
			res += s[i]
		return res

	# Time: O(n), space: O(1)
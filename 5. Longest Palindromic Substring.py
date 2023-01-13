class Solution:
	def longestPalindrome_optimal(self, s: str) -> str:
		# check the center of each word
		if not s:
			return ''

		n = len(s)
		longest_palindromic_count = 0
		longest_palindromic = ''

		for i in range(n):
			# if odd length
			left = right = i
			# try to expand both sides as far as possible
			while left >= 0 and right < n and s[left] == s[right]:
				if (right - left + 1) > longest_palindromic_count:
					longest_palindromic_count = right - left + 1
					longest_palindromic = s[left:right + 1]
				left -= 1  # expand to left side
				right += 1  # expand to right side

			# if even length:
			left, right = i, i + 1
			while left >= 0 and right < n and s[left] == s[right]:
				if (right - left + 1) > longest_palindromic_count:
					longest_palindromic_count = right - left + 1
					longest_palindromic = s[left:right + 1]
				left -= 1  # expand to left side
				right += 1  # expand to right side

		return longest_palindromic

	# time: O(n^2)
	# space: O(1)

	# BRUTE FORCE SOLUTION
	def longestPalindrome_brute_force(self, s: str) -> str:
		# a brute force Solution
		# try all possible substring and check if they are palindromic
		# time: O(n^3)

		# a single char is a palindromic
		def isValidPalindromic(string: str) -> bool:
			left, right = 0, len(string) - 1
			while left <= right:
				if string[left] != string[right]:
					return False
				left += 1
				right -= 1

			return True

		if not s or len(s) == 1:
			return s
		longest_palindromic_count = 0
		longest_palindromic = ''

		for i in range(len(s)):
			for j in range(i, len(s)):
				if isValidPalindromic(s[i:j]) and (j - i + 1 > longest_palindromic_count):
					longest_palindromic = s[i:j]
					longest_palindromic_count = j - i + 1

		return longest_palindromic

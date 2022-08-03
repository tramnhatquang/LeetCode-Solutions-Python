class Solution:
	def longestPalindrome(self, s: str) -> str:
		if not s:  # make sure we do not have empty string
			return 0
		n = len(s)
		longest_palindromic_count = 0  # since a character is a palindromic
		longest_palindromic = ''
		for i in range(n):
			# if odd length
			left, right = i, i
			while left >= 0 and right < n and s[left] == s[right]:
				if (right - left + 1) > longest_palindromic_count:
					longest_palindromic = s[left:right + 1]
					longest_palindromic_count = right - left + 1
				left -= 1
				right += 1

			# if even length
			left, right = i, i + 1
			while left >= 0 and right < n and s[left] == s[right]:
				# while left >= 0 and right < n and s[left] == s[right]:
				if (right - left + 1) > longest_palindromic_count:
					longest_palindromic = s[left:right + 1]
					longest_palindromic_count = right - left + 1
				left -= 1
				right += 1

		return longest_palindromic

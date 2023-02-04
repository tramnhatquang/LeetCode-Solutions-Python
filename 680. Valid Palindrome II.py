class Solution:
	def validPalindrome(self, s: str) -> bool:
     
	# Algo:
	# 1. Initialize two points art opposite ends of the string
	# 2. If the values at the left and right indexes mathc, move both toward the middle until they meet
	# 3. If the values at the left and right indexes don't match, skip one of the elements and check the rest of the string for a palindrome
	# 4. Skip the other element and check the rest of the string for a palindrome
	# 5. If no palindrome is found, return False. Else if, no more than one mismatche occurs throughout the traversal, return True.


		def check_palindrome(s, i, j):
			while i < j:
				if s[i] != s[j]:
					return False
				i += 1
				j -= 1

			return True

		i = 0
		j = len(s) - 1
		while i < j:
			# Found a mismatched pair - try both deletions

			if s[i] != s[j]:
				return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
			i += 1
			j -= 1

		return True

	# time: O(n)
	# space: O(1)

class Solution:
	def isPalindrome(self, s: str) -> bool:
		# approach 1: Use the built-in functions
		#   - Traverse the s and append only lowercase alphanumeric characters into a  new string
		#   - Check if the reverse of new string is equal to the new string
		# res = ''
		# for c in s:
		# 	if c.isalnum():
		# 		res += c.lower()
		#
		# return res == res[::-1]

		# time: O(n), space: O(n), n is the length of the string

		# approach 2: Two pointers technique
		# What if the interviewer wants me to implement the isalnum() function and reduce to space complexity to O(1)

		# an empty string is a palindrome
		if not s:
			return True

		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not self.is_alnum(s[left]):
				left += 1
			while left < right and not self.is_alnum(s[right]):
				right -= 1
			# print(left, right)
			if s[left].lower() != s[right].lower():
				return False

			left += 1
			right -= 1
		return True

	# time: O(n), space: O(1), n is the length of the input

	# implement the isalnum() function

	def is_alnum(self, c) -> bool:
		return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord(
			'z') or ord('1') <= ord(c) <= ord('9')

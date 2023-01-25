class Solution:
	def reverseVowels(self, s: str) -> str:
		# Use two pointers to solve this problem
		#   - left pointer points to the first index
		#   - right pointer points to the last index
		# move the left pointer to the right until it reaches a vowel
		# move the right pointer to the left until it reaches a vowel
		# swap them and increase left by 1, and decrement right by 1
		# keep doing that until left pointer is equal or larger than right pointer
		list_string = list(s)  # conver it into a list since string is immutable
		left = 0
		right = len(s) - 1
		while left < right:
			while left < right and list_string[left].lower() not in 'aeiou':
				left += 1
			while left < right and list_string[right].lower() not in 'aeiou':
				right -= 1
			# swap them
			list_string[left], list_string[right] = list_string[right], list_string[left]
			left += 1
			right -= 1

		return ''.join(list_string)
	# time: O(n)
	# space: O(n) # convert a string to a list

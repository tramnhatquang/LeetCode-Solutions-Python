class Solution:
	def canPermutePalindrome_two_passes(self, s: str) -> bool:
		"""
		Notice that:
			- A palindrome is read the same forward as backward
			- A palindrome can exist only when all the freq of all chars are even, or (all freq of chars are even except one is odd). If more than one odd freq, there is no palindrome
		"""
		# Two passes approach
		counter = Counter(s)
		count_odd = 0
		for num, freq in counter.items():
			if freq % 2 != 0:  # if the freq of a number is odd
				count_odd += 1

		return count_odd <= 1

	# time: O(n), n is length of string s
	# space: O(n)

	def canPermutePalindrome_one_pass(self, s: str) -> bool:
		# If the value of the entry just updated in map happens to be odd, we increment the value of count to indicate that one more character with odd number of occurrences has been found.But, if this entry happens to be even, we decrement the value of count to indicate that the number of characters with odd number of occurrences has reduced by one.

		# one pass approach
		freq_map = {}
		count_odd = 0
		for char in s:
			if char not in freq_map:
				freq_map[char] = 1
			else:
				freq_map[char] += 1

			if freq_map[char] % 2 != 0:
				count_odd += 1
			else:
				count_odd -= 1

		return count_odd <= 1
	# time: O(n)
	# space: O(n)

from collections import Counter


class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		if len(ransomNote) > len(magazine):
			return False

		# count all frequencies of characters
		counter = Counter(magazine)
		for char in ransomNote:
			# char is not in magazine -> cannot form
			if char not in counter:
				return False
			else:
				counter[char] -= 1
				if counter[char] < 0:
					return False
		return True

	# time: O(n), space: O(n)
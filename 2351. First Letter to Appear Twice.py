class Solution:
	def repeatedCharacter(self, s: str) -> str:
		# approach 1: Using a hash set
		#   - For each iteration, check if the char is in the hash set. If it is, then that char is the first letter to appear twice. Otherwise, append that letter to the hash set

		char_set = set()
		for char in s:
			if char in char_set:
				return char
			char_set.add(char)

		return None  # if not found

# time: O(n), space: O(n), n is the length of string

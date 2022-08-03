from collections import Counter


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		# approach 1: Sorting
		# 1. Sorting both strings. After sorting, characters of each string will be placed lexicographically. Two anagram words are the same after sorting. Check if the sorted strings are the same. If they are, return True. Otherwise, returns False
		#         if len(s) != len(t):
		#             return False

		#         lst_s, lst_t= list(s), list(t)
		#         lst_s.sort()
		#         lst_t.sort()
		#         return lst_t == lst_s

		# time: O(n log n), n = s.length() = t.length()
		# space: O(n) based on the sort you choose

		# approach 2: Hash Map
		# 1. Use a hash map to count the occurences of each chracter in s
		# 2. Loop over each character in t and check each chacracter in t if
		#   - If one character is not in the hash map, return False
		#   - If the character is in the hashmap, decrement its occurence. If the occurence < 0, that means we have more char's occurence in t than in s so we return False. Then, we keep doing until we reach the end of t. If nothing returns during the traversal, return tRUE

		if len(s) != len(t):
			return False

		# time: O(n), n is the length of s (s and t have the same length)
		# space: O(1), since we only contain up to 26 lowercase letters
		counter = Counter(s)
		for char in t:
			if char not in counter:
				return False
			else:
				counter[char] -= 1
				if counter.get(char) < 0:
					return False
		return True

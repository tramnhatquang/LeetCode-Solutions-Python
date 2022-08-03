from typing import *

class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		# approach 1: use two hash maps and keep track of the mappings between the pattern and the string
		# One hash map for the mapping characters to word and the other for mapping words to characters.
		# If the character is NOT in the character to word mapping, you additionally check whether that word is also in the word to character mapping.
		# If that word is already in the word to character mapping, then you can return False immediately since it has been mapped with some other character before.
		# Else, update both mappings.
		# If the character IS IN in the character to word mapping, you just need to check whether the current word matches with the word which the character maps to in the character to word mapping. If not, you can return False immediately.

		#         map_char_word = {}
		#         map_word_char = {}
		#         words = s.split()
		#         if len(words) != len(pattern):
		#             return False

		#         for char, word in zip(pattern, words):
		#             if char not in map_char_word:
		#                 if word in map_word_char:
		#                     return False
		#                 else:
		#                     map_char_word[char] = word
		#                     map_word_char[word] = char
		#             else:
		#                 if map_char_word[char] != word:
		#                     return False

		#         return True

		# time: O(N), N is the length of words or the number of characters in pattern
		# space: O(M), M is the number of unique words in S. O(1) since we only have at most 26 keys

		# approach 2: Using only one hash map
		# we can check ahead if the lengths of the sets of two given inputs are the same in case two words map to the same character or two characters map to the same words
		words = s.split()
		if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
			return False

		map_char_word = {}
		for char, word in zip(pattern, words):
			if char not in map_char_word:
				map_char_word[char] = word
			elif map_char_word[char] != word:
				return False

		return True

	# time: O(N), N is the length of words or the number of characters in pattern
	# space: O(M), M is the number of unique words in S. O(1) since we only have at most 26 keys

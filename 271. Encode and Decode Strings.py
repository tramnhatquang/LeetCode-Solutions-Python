from typing import *


class Codec:
	# Use a character out of the 256 ascii characters and maybe in the Unicode character.
	# We append that character between each string in the list of strings and returns a complete string after all
	# For decoding, we split out the string separated by that given unicode character

	#     def encode(self, strs: List[str]) -> str:
	#         """Encodes a list of strings to a single string.
	#         """
	#         return chr(258).join(strs)

	# def decode(self, s: str) -> List[str]:
	#     """Decodes a single string to a list of strings.
	#     """
	#     return s.split(chr(258))

	# approach 2: Use a general encoding and decoding patterns
	# 'abcd' -> encoded as '4#abcd'
	# 'sd' -> encoded as '2#sd'
	# complete string encoded as -> 4#abcd2#sd'

	# For decoding, we will skip each string based on the prefix length and the separated '#'

	def encode(self, strs: List[str]) -> str:
		"""Encodes a list of strings to a single string.
		"""
		res = ''
		for s in strs:
			res += str(len(s)) + '#' + s
		return res

	# time: O(n), space: O(n), n is the length of strings

	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		"""
		res = []
		i = 0
		while i < len(s):
			j = i
			# find where the string starts
			while s[j] != '#':
				j += 1
			length = int(s[i:j])
			res.append(s[j + 1:j + 1 + length])
			i = j + 1 + length
		return res

# time: O(n), space: O(n)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

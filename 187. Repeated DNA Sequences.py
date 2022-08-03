from typing import *


class Solution:
	def findRepeatedDnaSequences(self, s: str) -> List[str]:
		# approach 1: Linear scan + hash table
		# 1. move a sliding window of length L along the string of length N and increase its occurence in table if we get a macth. Otherwise, we set it to 1.
		# 2. Afer that, we look over the table and return all the substring whose occurence is larger than 1

		# This brute force approach is inefficient due to large memory and time consumption.
		# time: O((N- L)* L), which is O(N) if L = 10 (constant). If we use a general L. It is O((N- L)* L)
		# space: O((N−L)L) to keep the table, that results in \mathcal{O}(N)O(N) for the constant L = 10L=10.
		#         freq_table = {}

		#         for i in range(len(s) - 9):
		#             substring = s[i:i+10]
		#             freq_table[substring] = 1 + freq_table.get(substring, 0)

		#         res = []
		#         # loop over the table and append all the substrings whose occurence is larger than 1
		#         for substring, count in freq_table.items():
		#             if count > 1:
		#                 res.append(substring)

		#         return res

		# approach 2: Instead of using a table in approach 1, we can use a set instead

		res, substrings = set(), set()
		for i in range(len(s) - 9):
			substring = s[i:i + 10]
			if substring in substrings:
				res.add(substring)
			substrings.add(substring)

		return list(res)

# approach 3: Rabin-Karp + Bit mask manipulation are quite complicated

class Solution:
	def romanToInt(self, s: str) -> int:

		# APPROACH 1: RIGHT TO LEFT PASS
		# if we pay attention to the Roman representation
		# for two different numerical symbols, if the second symbol's value is less than the first symbol's,
		# e.g. VI -> sum = 5 + 1
		# However, if the second symbol's value is greater than the first symbol's
		# e.g. IV  -> sum = 5 - 1 = 4
		# sum += value(V) - value(I)
		# equivalent to sum += value(V) then sum -= value(C)
		# It hints us that we can start traversing the whole string backward from the end
		# we compare the symbol at i-th index with the one after it, we may add or subtract based on the observations we get above

		# Observe the following:
		# Without looking at the next symbol, we don't know whether or not the left-most symbol should be added or subtracted.
		# The right-most symbol is always added. It is either by itself, or the additive part of a pair.

		#         symbol_value = {
		#             'I' : 1,
		#             'V' : 5,
		#             'X' : 10,
		#             'L' : 50,
		#             'C' : 100,
		#             'D' : 500,
		#             'M' : 1000
		#         }

		#         # loop backward from right to left
		#         ans = symbol_value.get(s[-1])
		#         for i in range(len(s) - 2, -1, -1):
		#             if symbol_value[s[i]] < symbol_value[s[i+1]]:
		#                 ans -= symbol_value[s[i]]
		#             else:
		#                 ans += symbol_value[s[i]]

		#         return ans
		# TIME = SPACE = O(1) because the input <= 3999. If the length of input is N then time = O(N)

		# APPROACH 2: LEFT TO RIGHT BY LOOKING AT THE MAP VALUE

		symbol_value = {
			'I': 1,
			'IV': 4,
			'V': 5,
			'IX': 9,
			'X': 10,
			'XL': 40,
			'L': 50,
			'XC': 90,
			'C': 100,
			'CD': 400,
			'D': 500,
			'CM': 900,
			'M': 1000
		}

		ans = i = 0
		while i < len(s):
			if i < len(s) - 1 and s[i:i + 2] in symbol_value:
				ans += symbol_value[s[i:i + 2]]
				i += 2
			else:
				ans += symbol_value[s[i]]
				i += 1

		return ans

		# TIME = SPACE = O(1) as the first approach

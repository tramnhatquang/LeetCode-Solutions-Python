from typing import *


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		# approach 1: backtracking
		#   - Only add ')' to the string if the number of close parentheses is less than number of open parenethese.
		#   - We will use up to n number of open parenthese and n number of close parenthese
		#   - Only add '(' if open < n
		stack = []
		res = []

		def generate(open_par: int, close_par: int):
			if open_par == close_par == n:
				res.append(''.join(stack))
				return
			if open_par < n:
				stack.append('(')
				generate(open_par + 1, close_par)
				stack.pop()

			if close_par < open_par:
				stack.append(')')
				generate(open_par, close_par + 1)
				stack.pop()

		generate(0, 0)
		return res

# time = space = O(4^n / sqrt(n), n is the given input

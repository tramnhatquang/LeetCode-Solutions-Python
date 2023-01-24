from typing import *


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		# approach 1: backtracking
		#   - Only add ')' to the string if the number of close parentheses is less than number of open parenethese.
		#   - We will use up to n number of open parenthese and n number of close parenthese
		#   - Only add '(' if open < n
		# some exampleS:
		# () -> valid
		# ) -> invalid
		# ()) -> invalid
		# for each backtrack recursive call, we keep track of two additional states (number of open parenthesis, number of close parenthesis) -> both start at 0
		# we only append a new close parenthesis if number of open parenthesis > number of close parenthesis
		res = []

		def backtrack(openCount: int, closeCount: int, path: List[str]) -> None:
			if openCount == closeCount == n:  # base case
				res.append(''.join(path))
				return

			if openCount < n:
				path.append('(')
				backtrack(openCount + 1, closeCount, path)
				path.pop()

			# append a closing parenthesis
			if closeCount < openCount:
				path.append(')')
				backtrack(openCount, closeCount + 1, path)
				path.pop()

		backtrack(0, 0, [])
		return res


# time = space = O(4^n / sqrt(n), n is the given input
if __name__ == '__main__':
	s = Solution()
	print(s.generateParenthesis(2))  # -> ['(())', '()()']

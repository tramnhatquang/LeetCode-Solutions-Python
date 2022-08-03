from typing import List


class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		# APPROACH 1: use a stack to solve this problem
		# 1. keep appending numbers into the stack
		# 2. if we meet an operator, we pop the last two numbers from the stack and apply the operator on those. After that, we append back the result into the stack
		# 3. Repeat step 1 and 2 until the stack only has 1 element
		stack = []

		for token in tokens:
			# since there are only numbers and operators in the stack
			if token not in '+-*/':
				stack.append(int(token))
			else:
				num2, num1 = stack.pop(), stack.pop()
				if token == '+':
					stack.append(num1 + num2)
				elif token == '-':
					stack.append(num1 - num2)
				elif token == '*':
					stack.append(num1 * num2)
				else:  # token == '/'
					stack.append(int(num1 / num2))

		return stack[0]

# time: O(N) where N is the length of tokens
# SPace: O(N) since stack can contain at most N tokens in the worst scenario

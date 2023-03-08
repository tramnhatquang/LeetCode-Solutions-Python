class Solution:
	def calculate_stack(self, s: str) -> int:
		"""
		- Since we do not have parentheses (), we only take care of +, -, *, //
		- If the curr operation is addition (+) or substraction (-), then the expression is evaulated based on the precedence of the next operation
		-
		"""
		stack = []
		curr_num = 0
		prev_sign = '+'
		for i, char in enumerate(s):
			# char = s[i]
			if char.isdigit():
				curr_num = curr_num * 10 + int(char)
			if char in '+-*/' or i == len(s) - 1:  # char is '+-*/'
				if prev_sign == '-':
					stack.append(-curr_num)
				elif prev_sign == '+':
					stack.append(curr_num)
				elif prev_sign == '*':
					stack.append(stack.pop() * curr_num)
				else:
					stack.append(int(stack.pop() / curr_num))
				curr_num = 0
				# update a new sign
				prev_sign = char

		return sum(stack)
# time: O(n) = space, n is length of string

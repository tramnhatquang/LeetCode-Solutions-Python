class Solution:
	def minAddToMakeValid(self, s: str) -> int:
		# APPROACH: One pass + stack
		# 1. Iterating the string from left to right and visit each character. If we meet an open parenthesis, we append it to the stack. If we meet a close parenthesis, we check if the top of the stack is an open one, then continue. If we do not have any open one, we also append it
		# 2. The minimum add is the length of the stack

		#         stack = []
		#         for char in s:
		#             if char == ')':
		#                 if stack and stack[-1] == '(':
		#                     stack.pop()
		#                     continue
		#             stack.append(char)

		#         return len(stack)

		# time: O(n), N is length of S
		# space: O(1), we use constant space

		# APPROACH 2: One pass + keep track of the open and close parenthesis
		# 1. we keep two variables, one to count the open parentheses, one to count the close parenthese.
		# 2. We iterate each parenthesis in the string
		#    - if there is an open, open += 1
		#   - if there is a close: check
		# - if the open_count > 0: open -= 1
		# - else, close += 1

		# the min add =  open + close

		open_count = close_count = 0
		for char in s:
			if char == '(':
				open_count += 1
			else:
				if open_count > 0:
					open_count -= 1
				else:
					close_count += 1
		return open_count + close_count

	# time: O(n), space: O(1)

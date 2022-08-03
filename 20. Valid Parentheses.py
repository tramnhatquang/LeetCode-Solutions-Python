from typing import *
class Solution:
	def isValid(self, s: str) -> bool:
		# APPROACH 1: Stack
		# 1. Initialize a dictionary that maps a specific open bracket to its clos e bracket
		# 2. Loop over the given string
		#   - Append all the open brackets into the stack
		#   - If you meet a close bracket, pop out the top open bracket from the stack and see if they match to each other. If they do not match, return False. Otherwise, we continue the process until we reach the end of the s
		# 3. If we have more open brackets than close ones, the stack still has elements. It means we need to return false. If the stack is empty, we have balance brackets so we return True

		if not s:
			return False
		stack = []
		open_to_close = {'(': ')',
		                 '[': ']',
		                 '{': '}'}

		for bracket in s:
			# append all the open brackets
			if bracket in open_to_close:
				stack.append(bracket)
			else:
				if stack and open_to_close[stack[-1]] == bracket:
					stack.pop()
				else:
					# we either do not have any available open brackets or the open and close brackets do not match
					return False
		# if stack still has values, we return False. Otherwise, return True
		return not stack

	# time: O(n), n is the length of string
	# space: O(n) in the worst case scenario

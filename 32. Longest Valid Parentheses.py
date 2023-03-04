class Solution:
	def longestValidParentheses_stack(self, s: str) -> int:
		"""
		Using a stack to solve this problem.
		 - We start with a stack containing -1 to handle the edge case of a valid parentheses substring starting at the beginning of the string (e.g., the string "()(()" should return 2, not 4).
		- We initialize the maximum length to 0 and scan the string from left to right. For each character, we check if it's an open parenthesis or a close parenthesis. If it's an open parenthesis, we push its index onto the stack. If it's a close parenthesis, we pop the index of the last open parenthesis from the stack and compute the length of the valid parentheses substring as the difference between the current index and the index on top of the stack. We update the maximum length of the valid parentheses substring seen so far, and continue with the next character. At the end of the loop, we return the maximum length.
		"""
		# start with -1 to handle edge case of "()" at beginning of string
		# append (-1) to handle the edge case when we have valid substring like (() or () at the beginining
		stack = [-1]
		max_length = 0
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			else:
				if stack:
					stack.pop()
					if stack:  # if stack still has element, find the max length from the top of stack
						max_length = max(max_length, i - stack[-1])
					else:
						stack.append(i)
				else:
					stack.append(i)

		return max_length


# time = O(n), n is length of arr
# space: O(n)


def longestValidParentheses_brute_force(self, s: str) -> int:
	max_length = 0
	# check every possible non-empty even length substring
	for i in range(len(s)):
		for j in range(i + 2, len(s) + 1, 2):
			if self.isValid(s[i:j]):
				max_length = max(max_length, j - i)

	return max_length


def isValid(self, s: str) -> bool:
	stack = []
	for char in s:
		if char == '(':
			stack.append(char)
		else:
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				return False
	return not stack

class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
		# APPROACH 1: Two passes
		# 1. In the first pass from left to right, we want to remove the excessive close parentheses by keeping track of the balace parentheses and the number of open parentheses for the second pass
		# We iterate through each character in the string and whenever we meet an open parenthese, we increment the balance += 1, and the opne_paren += 1. if we meet a close parenthesis, we decrement the balance parenthese (balance -= 1) and at any time if the balance is negative, we move on to the next character. Otherwise, we add that character to the result.
		# 2. For the second pass, we want to remove all the excessive open parentheses by computing the open_to_keep parentheses
		# open_keep = total_open - balance
		# We re-iterate the array again and decrement the opne_to keep by 1 whenever we meet an open parenthesis. If the open_to keep is negative, we have to get rid of that open parenthesis and move on.
		#         char_list = []
		#         open_seen = balance = 0

		#         # Remove all the invalid ')'
		#         for char in s:
		#             if char == '(':
		#                 open_seen += 1
		#                 balance += 1
		#             elif char == ')':
		#                 if balance == 0:
		#                     continue
		#                 balance -= 1
		#             print(balance)
		#             # append the char in the char_list
		#             char_list.append(char)

		#         # # remove all the right most '('
		#         result = []
		#         open_to_keep = open_seen - balance
		#         for char in char_list:
		#             if char == '(':
		#                 open_to_keep -= 1
		#                 if open_to_keep < 0:
		#                     continue
		#             result.append(char)

		#         return ''.join(result)

		# APPROACH 2:
		# Convert string to list, because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
		# Iterate through list
		# Keep track of indices with open parentheses in the stack. In other words, when we come across open parenthesis we add an index to the stack.
		# When we come across close parenthesis we pop an element from the stack. If the stack is empty we replace current list element with an empty string
		# After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
		# Convert list to string and return
		stack = []
		word = list(s)
		for i in range(len(word)):
			if word[i] == "(":
				stack.append(i)
			elif word[i] == ")":
				if stack:
					stack.pop()
				else:
					word[i] = ""
		for idx in stack:
			word[idx] = ""
		return "".join(word)

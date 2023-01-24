from typing import List


def letter_combinations_of_phone_number(digits: str) -> List[str]:
	# WRITE YOUR BRILLIANT CODE HERE

	res = []
	digits_to_char = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
					  '9': 'wxyz'}

	def dfs(index: int, path: List[str]) -> None:
		if index == len(digits):  # base case
			res.append(''.join(path))
			return

		possible_number = digits[index]
		for char in digits_to_char[possible_number]:
			path.append(char)
			dfs(index + 1, path)
			path.pop()  # for backtracking, pop the additional state

	dfs(0, [])
	return res
# The time complexity of a backtracking algorithm is the number of nodes in the state-space tree multiplied by the operation at each node. In the worse case where we only have 7s and 9s in the input phone number, each node has 4 children. And the height of the tree is the number of digits of the phone number. Therefore the tree has maximum of 4^n nodes where n is the number of digits of the phone number. We also need O(n) to build a new string when we reach the leaf node so the total complexity is O(4^n * n).

# time: O(4^n * n), where n is the number of digits of the phone number

# space: O(n)

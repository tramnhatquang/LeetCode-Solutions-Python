from typing import List

"""
Find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

Input: 2
Output: ["aa", "ab", "ba", "bb"]

Input: 4
Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
"""


def letter_combination(n: int) -> List[str]:
	# WRITE YOUR BRILLIANT CODE HERE
	res = []

	def backtrack(curr: List[str]) -> None:
		# base case
		if len(curr) == n:
			res.append(''.join(curr))
			return

		for char in ['a', 'b']:
			curr.append(char)
			backtrack(curr)
			curr.pop()  # pop the current element

	backtrack([])
	return res

# time: O(2^n* n), For each node there are a maximum of 2 children. The height of the tree is n. The number of nodes is 2^n-1 (see the "perfect binary tree" section of Everything about trees for a quick review). It takes O(n) to join the n characters at each leaf node. So the overall time complexity is O(2^n*n).
# space: O(n)

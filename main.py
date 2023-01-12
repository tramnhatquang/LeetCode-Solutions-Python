import collections
import math
from typing import *


class TreeNode:

	def __init__(self, val=0, left=None, right=None) -> None:
		self.val = val
		self.left = left
		self.right = right


def sumOfLeftLeaves(root: TreeNode) -> int:
	if root is None:
		return 0

	def process_subtree(subtree):

		# Base case: This is a leaf node.
		if subtree.left is None and subtree.right is None:
			return subtree.val

		# Recursive case: We need to add and return the results of the
		# left and right subtrees.
		total = 0
		if subtree.left:
			total += process_subtree(subtree.left)
		if subtree.right:
			total += process_subtree(subtree.right)
		return total

	# Call the recursive function on the root node to start the process.
	# We need to be careful of the case that the root is empty.
	return process_subtree(root)


def validateBST(root: TreeNode) -> bool:
	def helper(root: TreeNode, lower: float, upper: float) -> bool:
		# an empty BST is a valid one
		if not root:
			return True

		# the node's val cannot be less than lower or equ
		if root.val <= lower or root.val >= upper:
			return False

		# The left and right subtree must also be valid.
		return (helper(root.right, root.val, upper) and
				helper(root.left, lower, root.val))

	return helper(root, -math.inf, math.inf)


def groupAnagrams(arr: List[str]) -> List[List[str]]:
	# map = collections.defaultdict(list)
	#
	# for string in arr:
	# 	map[tuple(sorted(string))].append(string)
	#
	# return list(map.values())

	# since we only deal with lowercase letters (26 letters)
	# can think of a list whose size is 26 and find the occurrences of each
	# string
	map = collections.defaultdict(list)
	for string in arr:
		count = [0] * 26
		for char in string:
			count[ord(char) - ord('a')] += 1
		map[tuple(count)].append(string)

	return list(map.values())


if __name__ == '__main__':
	arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(groupAnagrams(arr))

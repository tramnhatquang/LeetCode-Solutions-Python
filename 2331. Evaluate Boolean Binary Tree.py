from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def evaluateTree(self, root: Optional[TreeNode]) -> bool:
		"""
		Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
		Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
		"""
		# approach 1: Recursion
		# check if root is a leaf node
		if not root.left and not root.right:
			return root.val  # in python, 1 is True, 0 is False

		# if the root is not a leaf node
		if root.val == 2:
			return self.evaluateTree(root.left) or self.evaluateTree(
				root.right)  # use the 'OR' operation for leaf and right subtrees
		else:
			# root.val == '3'
			# use the 'AND' operation for leaf and right subtree
			return self.evaluateTree(root.left) and self.evaluateTree(
				root.right)

# time = space = O(n), n is the total nodes in the BT

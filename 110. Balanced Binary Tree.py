from typing import *
from collections import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isBalanced(self, root: TreeNode) -> bool:

		# approach 1: Do a top-down recursion. For each node, we calulate the
		# height of its left and right subtrees. Check if these heights are no
		# more than 1 time: O(n log n), n is the total nodes in the BT space:
		# O(n) for the recursive stack

		#         if not root: # an empty tree is a balanced tree
		#             return True

		#         left_depth = self.get_depth(root.left)
		#         right_depth = self.get_depth(root.right)
		#         if abs(left_depth - right_depth) > 1:
		#             return False

		#         return self.isBalanced(root.left) and self.isBalanced(root.right)

		#     def get_depth(self, root: TreeNode) -> int:
		#         if not root:
		#             return 0

		# return max(self.get_depth(root.left), self.get_depth(root.right))
		# + 1

		# approach 2: find the height of each node but from the bottom-up
		# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
		# For every node, its left and right subtrees must be balance and the height of them differ no more than 1
		# if the height is more than 1, we can return False
		# if one of the subtrees are unbalanced, we can break the recursive call early instead of keeping checking every node in the top down approach

		def get_depth(root: TreeNode):
			if not root:  # an empty tree is a balanced tree
				return True
			# we use -1 as a signal of getting unbalanced subtrees or when the height between subtrees are more than 1

			left_depth = get_depth(root.left)
			if left_depth == -1:
				return -1
			right_depth = get_depth(root.right)
			if right_depth == -1:
				return -1
			if abs(left_depth - right_depth) > 1:
				return -1

			return max(left_depth, right_depth) + 1

		return get_depth(root) != -1

	# time: O(n), n is total nodes in the BT
	# space: O(n)

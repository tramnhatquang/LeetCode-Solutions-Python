from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def mergeTrees(self, root1: Optional[TreeNode],
	               root2: Optional[TreeNode]) -> Optional[TreeNode]:
		# approach 1: Using recursion
		# base case: if two nodes are both None, return None
		# if one of those  is None, return the other one
		# Recursively merge both trees starting from the root

		if root1 and root2:
			root = TreeNode(root1.val + root2.val)
			root.left = self.mergeTrees(root1.left, root2.left)
			root.right = self.mergeTrees(root1.right, root2.right)
			return root
		else:
			# one of the nodes are not None or both are None
			return root1 or root2

# time: O(n), n is the total nodes in the tree
# space: O(n)

from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[
		TreeNode]:
		# approach 1: Recursion
		# - Build based on the pre-order and in-order given
		# - the first node of the pre-order is always the root node
		if not preorder or not inorder:
			return None

		root = TreeNode(preorder[0])
		# find the index of the root in the inorder traversal
		# all elements to its left belong to the left subtree
		# all elements to its right belong to the right subtree
		mid = inorder.index(preorder[0])
		root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
		root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

		return root

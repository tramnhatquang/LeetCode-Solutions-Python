# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def deleteNode(self, root: TreeNode, key: int) ->TreeNode:
		if not root:
			return None

		if root.val < key:
			root.right = self.deleteNode(root.right, key)
		elif root.val > key:
			root.left = self.deleteNode(root.left, key)
		else:
			# root.val == key
			# Case 1: when the removed node is a leaf
			if not root.right and not root.left:
				return None

			# Case 2: when the removed has one child (left or right child)
			if not root.left:
				return root.right
			if not root.right:
				return root.left

			# Case 3: when the removed node has two children (find the in-order sucessor of the current (removed) node)
			successor = root.right  # root.right is not None
			while successor.left:
				successor = successor.left
			root.val = successor.val
			root.right = self.deleteNode(root.right, successor.val)
		return root

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
		# Approach: We call the funnction sameTRee() for every node in the
		# original BT. We refer to the sameTree() to make sure the subRoot is
		# an actual sub root in the BT

		# Time: O(M * N), where M is the number of nodes in binary tree root,
		# N is the number of nodes in binary tree subRoot Space: O(H), where H
		# is the height of binary tree root
		if not subRoot:
			return True
		if not root:
			return False
		if self.sameTree(root, subRoot):
			return True
		return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


	def sameTree(self, root1: TreeNode, root2: TreeNode) -> bool:
		if not root1 and not root2:
			return True
		if not root1 or not root2:
			return False
		return root1.val == root2.val and self.sameTree(root1.left, root2.left) and self.sameTree \
			(root1.right, root2.right)

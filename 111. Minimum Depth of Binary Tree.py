# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def minDepth(self, root: Optional[TreeNode]) -> int:
		# dfs, recursive approach
		# base cases
		if not root:
			return 0
		# check if we are at a leaf node
		if not root.right and not root.left:
			return 1

		# if the left subtree is None, recr on the right subtree
		if not root.left:
			return 1 + self.minDepth(root.right)
		# if the right subtree is None, recr on the left subtree
		if not root.right:
			return 1 + self.minDepth(root.left)

		return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
	# time = space = O(n), n is the total nodes in the BT

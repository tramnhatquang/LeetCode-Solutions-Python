import collections


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def invertTree(self, root: TreeNode) -> None:
		# approach 1: recursion,
		# Stratting from the root, we recursively invert the left subtree by the right subtree. Similarly, we invert the right subtree by the left subtree
		# if not root:
		# 	return None
		# root.left, root.right = self.invertTree(root.right), self.invertTree(
		# 	root.left)
		# return root

		# time: O(n), n is the number of nodes in the tree
		# space: O(h), h is the height of the tree. In the worst case, O(h) is equivalent to O(n)

		# approach 2: DFS, iterative
		# if not root:
		#     return None
		# stack = [root]
		# while stack:
		#     node = stack.pop()
		#     node.left, node.right = node.right, node.left
		#     for node in [node.left, node.right]:
		#         if node:
		#             stack.append(node)
		# return root

		# approach 3: BFS, iterative
		if not root:
			return None
		q = collections.deque([root])
		while q:
			node = q.popleft()
			node.left, node.right = node.right, node.left
			for node in [node.left, node.right]:
				if node:
					q.append(node)

		return root

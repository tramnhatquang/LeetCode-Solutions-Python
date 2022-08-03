from typing import *
from collections import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def maxDepth(self, root: TreeNode) -> int:

		# approach 1: Recursion + DFS
		# if the node is None, return 0
		#         if not root:
		#             return 0
		#         left_depth = self.maxDepth(root.left)
		#         right_depth = self.maxDepth(root.right)
		#         return max(left_depth, right_depth) + 1

		# time: O(n), n is total nodes in the BT
		# space: O(n) when the BT is unbalanced (skewed left or right)

		# approach 2: DFS + Iteration
		# if not root:
		#     return 0
		# res = 0
		# stack = [(root, 1)]
		# while stack:
		#     curr_node, curr_depth = stack.pop()
		#     if not curr_node.left and not curr_node.right: # check if we reach a leaf node
		#         res = max(res, curr_depth)
		#     for node in [curr_node.right, curr_node.left]:
		#         if node:
		#             stack.append((node, curr_depth + 1))
		# return res

		# approach 3: BFS + iteration
		res = 0
		if not root:
			return 0
		q = deque([(root, 1)])
		while q:
			curr_node, curr_depth = q.popleft()
			if not curr_node.left and not curr_node.right:
				res = max(res, curr_depth)
			for node in [curr_node.left, curr_node.right]:
				if node:
					q.append((node, curr_depth + 1))
		return res

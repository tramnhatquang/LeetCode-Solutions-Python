from collections import *
from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def rightSideView_dfs_recursive(self, root: Optional[TreeNode]) -> List[int]:
		# do DFS, but will visit the rightmost node of each level first, then the left node. For each level, we only get the rightmost node.
		# To get the rightmost node of each level, we use a trick to check if the size(result) == level, then we add the rightmost node
		res = []

		def dfs(root: TreeNode, level: int) -> None:
			if not root:
				return
			if level == len(res):
				res.append(root.val)

			dfs(root.right, level + 1)
			dfs(root.left, level + 1)

		dfs(root, 0)
		return res

	# time = space = O(n)

	def rightSideView_bfs_iterative(self, root: Optional[TreeNode]) -> List[int]:
		# approach 1: BFS
		# 1. For each level of the binary tree, we only append the right most non-null node. Keep going level by level, we will have the desired result
		res = []
		if not root:
			return res

		queue = deque([root])
		while queue:
			level_size = len(queue)
			# append all the nodes' values in the same level
			curr_level = []
			for _ in range(level_size):
				node = queue.popleft()
				curr_level.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			res.append(curr_level[-1])

		return res

# time = space =  O(n), n is the number of nodes in BT

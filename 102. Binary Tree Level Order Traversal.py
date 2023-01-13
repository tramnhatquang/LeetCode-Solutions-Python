# Definition for a binary tree node.
from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


from typing import List, Optional


class Solution:
	def levelOrder_bfs_iterative(self, root: Optional[TreeNode]) -> List[List[
		int]]:

		# solve using BFS, iterative
		res = []
		if not root:
			return res

		level = 0
		# use both the node and its level as key in the queue
		queue = deque([root])

		while queue:
			curr_length = len(queue)
			# do logic for the curr level
			# append a new list into the result
			res.append([])
			for _ in range(curr_length):
				node = queue.popleft()

				# append it to the res
				res[level].append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			level += 1

		return res

	# time = space = O(n)

	def levelOrder_dfs_recursive(self, root: Optional[TreeNode]) -> List[
		List[
			int]]:
		levels = []

		def dfs(node, level):
			if node:
				if len(levels) == level:
					levels.append([])
				levels[level] += [node.val]
				dfs(node.left, level + 1)
				dfs(node.right, level + 1)

		dfs(root, 0)
		return levels

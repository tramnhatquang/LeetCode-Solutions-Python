from collections import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:

	def maxDepth_dfs_iterative(self, root: Optional[TreeNode]) -> int:
		# DPS + iteration
		if not root:
			return 0

		max_depth = 1  # include the root since it's not null
		stack = [(root, 1)]
		while stack:
			node, curr_depth = stack.pop()

			# check if the curr node is a leaf or not
			if not node.left and not node.right:
				max_depth = max(max_depth, curr_depth)

			# append its left and right childs
			if node.left:
				stack.append((node.left, curr_depth + 1))
			if node.right:
				stack.append((node.right, curr_depth + 1))

		return max_depth

	# time = space = O(n), n is the total nodes in the BT

	def maxDepth_dfs_recursive(self, root: Optional[TreeNode]) -> int:
		# recusrion + dfs
		if not root:
			return 0

		left_depth = self.maxDepth(root.left)
		right_depth = self.maxDepth(root.right)
		return max(left_depth, right_depth) + 1

	# we need to put (+1) to count the current leaf node into the max_depth
	# time = space = O(n)

	def maxDepth_bfs_iterative(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0

		# root is not null when starting and its curr depth = 1
		queue = deque([(root, 1)])
		max_depth = 1  # count the root at first
		while queue:
			curr_length = len(queue)

			# curr_length gives the number of nodes in the curr level
			for _ in range(curr_length):
				node, curr_depth = queue.popleft()

				# check if we have a leaf node
				if not node.left and not node.right:
					max_depth = max(max_depth, curr_depth)
				if node.left:
					queue.append((node.left, curr_depth + 1))
				if node.right:
					queue.append((node.right, curr_depth + 1))

		return max_depth

# time = space = O(n)

# time: O(n) = space

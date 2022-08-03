from collections import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def widthOfBinaryTree(self, root: TreeNode) -> int:
		# the key to solve this problem is to mark the the column index for each level in the binary tree. In a binary tree, a node can have at most two children nodes. If the node's index is C, then the left node's index is (C * 2) and the right node's index is (C * 2) + 1
		# for each level, we only need to keep track the first index and last index. The width of each level is (R - L + 1) where R is the right-most index, L is the left-most index
		# APPROACH 1: BFS

		if not root:
			return 0

		max_width = 0
		queue = deque([(root, 0)])

		while queue:
			level_size = len(queue)
			start_index = queue[0][1]  # start index of the queue
			for _ in range(level_size):
				node, curr_index = queue.popleft()

				if node.left:
					queue.append((node.left, curr_index * 2))
				if node.right:
					queue.append((node.right, curr_index * 2 + 1))

			# compute the max width of each level
			max_width = max(max_width, curr_index - start_index + 1)

		return max_width

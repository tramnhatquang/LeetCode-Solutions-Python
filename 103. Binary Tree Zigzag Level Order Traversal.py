from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

		# Approach 1: BFS
		# 1. Do a normal BFS through each level of the BT
		# 2. for even level, we keep the same list of nodes. However, for the odd level, we reverse the list of nodes. At the end of each level, we append the level into the result list
		#         even_level = True
		#         if not root:
		#             return []
		#         result = []
		#         queue = deque([root])
		#         while queue:
		#             level_size = len(queue)
		#             node_list = []
		#             for _ in range(level_size):
		#                 node = queue.popleft()
		#                 node_list.append(node.val)
		#                 if node.left:
		#                     queue.append(node.left)
		#                 if node.right:
		#                     queue.append(node.right)
		#             if even_level:
		#                 result.append(node_list)
		#             else:
		#                 result.append(node_list[::-1])

		#             # change the level (odd - > even, even -> odd)
		#             even_level = not even_level

		#         return result

		# time: O(n), N is the number of nodes in BT
		# space: O(N). The worst case scenario is a skweed tree

		## APPROACH 2: DFS
		levels = []

		# Depth first search
		# At each depth, append value to that element in the array

		def dfs(node, depth):
			if not node:
				return
			if len(levels) == depth:
				levels.append([])
			levels[depth].append(node.val)
			dfs(node.left, depth + 1)
			dfs(node.right, depth + 1)

		dfs(root, 0)
		for i in range(len(levels)):
			if i % 2 == 1:
				levels[i].reverse()

		return levels

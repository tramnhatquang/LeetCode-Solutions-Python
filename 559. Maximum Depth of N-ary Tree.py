# Definition for a Node.
class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children


class Solution:
	def maxDepth(self, root: 'Node') -> int:
		# APPROACH 1: DFS to find the longest path from the root to the furthest leaf node
		# We will use the stack to keep track of both the current processed node and the current depth so far. For each child of the current node, we append both the child node and depth + 1 into the stack
		# At any iteration, if we reach a leaf node, we return the depth. At that time, the depth represents the max depth
		#         if not root: # base case
		#             return 0

		#         max_depth = 0
		#         stack = [(root, 1)]
		#         while stack:
		#             node, curr_depth = stack.pop()

		#             max_depth = max(max_depth, curr_depth)

		#             for child in node.children:
		#                 stack.append((child, curr_depth + 1))

		#         return max_depth

		# time: O(n), N is the number of nodes in N-ary tree. In the worst case, the tree is skewed.
		# space: O(N)

		# APPROACH 2: RECURSION
		if not root: return 0
		if not root.children: return 1
		height = [self.maxDepth(node) for node in root.children]
		return max(height) + 1

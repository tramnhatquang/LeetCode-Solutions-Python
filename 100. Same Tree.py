from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:

	def isSameTree_dfs_recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

		# approach 1: Top-down recursion Compare the corresponding nodes
		# together. After that, continue to compare their left and right
		# subtrees base case if not p and not q: # both compared nodes are
		# None return True if not p or not q: # one of the compared nodes is
		# None, the other is not return False
		# base cases
		if not p and not q:
			return True
		if not p or not q:
			return False

		return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

	def isSameTree_dfs_iterative_1(self, p: TreeNode, q: TreeNode) -> bool:

		# approach 2: Top down iterative, DFS
		# time = space = O(n)
		stack = [(p, q)]
		while stack:
			node1, node2 = stack.pop()
			if node1 and node2 and node1.val == node2.val:
				stack.append((node1.left, node2.left))
				stack.append((node1.right, node2.right))
			elif node1 != node2:
				return False
		# node1 = node2 = None, we should continue to check
		return True

	def isSameTree_dfs_iterative_2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		stack = [(p, q)]
		while stack:
			node1, node2 = stack.pop()
			# if both nodes are null, continue processing other nodes
			if not node1 and not node2:
				continue
			# if one of nodes is empty, the other one is not
			if not node1 or not node2:
				return False
			# two nodes' values are different
			if node1.val != node2.val:
				return False
			stack.append((node1.left, node2.left))
			stack.append((node1.right, node2.right))

		return True

# time: O(n), space: O(n)

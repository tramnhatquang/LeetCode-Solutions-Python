from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

		# approach 1: Top-down recursion Compare the corresponding nodes
		# together. After that, continue to compare their left and right
		# subtrees base case if not p and not q: # both compared nodes are
		# None return True if not p or not q: # one of the compared nodes is
		# None, the other is not return False

		# return p.val == q.val and self.isSameTree(p.left, q.left) and
		# self.isSameTree(p.right, q.right)

		# approach 2: Top down iterative, BFS
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

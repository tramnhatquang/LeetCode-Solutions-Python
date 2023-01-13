# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:

	def isSymmetric_bfs_iterative(self, root: Optional[TreeNode]) -> bool:
		# do the bfs + iteration

		# bfs will be faster than dfs in this case, since we can return False immediately before traversing deeply the BT

		if not root:
			return True

		stack = [(root.left, root.right)]

		while stack:
			node1, node2 = stack.pop()
			if not node1 and not node2:
				continue
			if not node1 or not node2:  # they are not symmetric
				return False
			if node1.val != node2.val:
				return False
			else:
				# append left and right subtrees of two nodes into the stack
				stack.append((node1.left, node2.right))
				stack.append((node1.right, node2.left))

		# if the loop does not return False, that means we have a symmetric tree
		return True

	# time: O(n) = spaace, n is the total of nodes in the BT

	def isSymmetric_dfs_recursive(self, root: Optional[TreeNode]) -> bool:

		# recursive approach
		# think about parsing the left subtree and right subtree in the helper/dfs function
		# think about your base cases
		# how to make recursive calls so that eventually the function comes to the base cases

		def dfs(node1, node2) -> bool:
			# establish base cases
			if not node1 and not node2:
				return True
			if not node1 or not node2:
				return False

			# recursively call dfs on the left and right subtrees until we reach the base cases
			return node1.val == node2.val and dfs(node1.left,
												  node2.right) and dfs(
				node1.right, node2.left)

		# sanity check the root node
		if not root:
			return True  # an empty tree is a symmetric one

		return dfs(root.left, root.right)

# time: O(n) = space, n is total nodes in the binary tree

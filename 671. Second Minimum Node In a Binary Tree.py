from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
		# approach 1: traverse the tree and record every unique values in the BT

		values_set = set()

		def dfs(root: TreeNode) -> None:
			if root:
				values_set.add(root.val)
				dfs(root.left)
				dfs(root.right)

		dfs(root)
		min1, ans = root.val, float('inf')
		for v in values_set:
			if min1 < v < ans:
				ans = v

		return ans if ans < float('inf') else -1

from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		# APPROACH 1: Preoreder traversal and choose left middle node as a root
		if not nums:
			return None

		def helper(left: int, right: int) -> TreeNode:
			if left > right:
				return None

			mid = (left + right) // 2
			# choose the middle value as the value for the root node
			root = TreeNode(nums[mid])
			root.left = helper(left, mid - 1)
			root.right = helper(mid + 1, right)
			return root

		return helper(0, len(nums) - 1)

	# time: O(n), n is the number of nodes in the tree
	# space: O(log n) since the tree is balanced

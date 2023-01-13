# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def searchBST_ietrative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		while root is not None and root.val != val:
			if val < root.val:
				root = root.left
			else:
				root = root.right
		return root

	# time: O(h) like the recursive approach
	# space: O(1)

	def searchBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		if not root:
			return None

		if root.val == val:
			return root
		elif root.val > val:
			return self.searchBST(root.left, val)
		else:
			return self.searchBST(root.right, val)

# $ time = space = O(h) where h is the height of tree. It returns O(log n) in the average case, and O(n) in the worst
# case

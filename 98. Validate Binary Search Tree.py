# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:

		def validate(root, lower=-math.inf, upper=math.inf) -> bool:
			# base case
			if not root:  # an empty node must be within the lower and upper bound
				return True

			# the node's val must be always between the lower and upper bound
			# we use the equal sign on both expressions since all left nodes must be less than root's val and all right nodes must be larger than root.val
			if root.val <= lower or root.val >= upper:
				return False

			# recursively check the left and right subtrees
			return validate(root.left, lower, root.val) and validate(root.right, root.val, upper)

		return validate(root)

	# time: O(n), space: O(n), n is total nodes in BST

	def isValidBST_iterative(self, root: Optional[TreeNode]) -> bool:
		# use dfs iterative
		if not root:  # an empty tree is a valid BST
			return True

		stack = [(root, -math.inf, math.inf)]

		while stack:
			root, lower, upper = stack.pop()

			if root.val <= lower or root.val >= upper:
				return False

			if root.left:
				stack.append((root.left, lower, root.val))
			if root.right:
				stack.append((root.right, root.val, upper))

		return True

	# time: O(n), space: O(n)

	def isValidBST_inorder_iterative(self, root: TreeNode) -> bool:
		stack, prev = [], -math.inf

		while stack or root:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			# If next element in inorder traversal
			# is smaller than the previous one
			# that's not BST.
			if root.val <= prev:
				return False
			prev = root.val
			root = root.right

		return True

# time: O(n), space: O(n)

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		diameter = 0

		def longest_path(node):
			if not node:
				return 0
			nonlocal diameter
			# recursively find the longest path in
			# both left child and right child
			left_path = longest_path(node.left)
			right_path = longest_path(node.right)

			# update the diameter if left_path plus right_path is larger
			diameter = max(diameter, left_path + right_path)

			# return the longest one between left_path and right_path;
			# remember to add 1 for the path connecting the node and its parent
			return max(left_path, right_path) + 1

		longest_path(root)
		return diameter


if __name__ == '__main__':
	s = Solution()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right = TreeNode(3)

	print(s.diameterOfBinaryTree(root))

if __name__ == '__main__':
	s = Solution()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right = TreeNode(3)

	print(s.diameterOfBinaryTree(root))

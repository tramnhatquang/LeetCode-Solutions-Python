class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def inorderSuccessor_optimal_way(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

		successor = None

		while root:

			if p.val >= root.val:
				root = root.right
			else:
				successor = root
				root = root.left

		return successor

	# time: O(n), n is total nodes in the BST, in case we can have a skewed tree
	# space: O(1)
	def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
		# use an arr to store all the nodes in the inorder traversal
		res = []

		def inorder(root):
			if root:
				inorder(root.left)
				res.append(root)
				inorder(root.right)

		inorder(root)

		# check if we have a node like p and return its in-order successor
		# inorder traversal in BST -> sorted array
		for i in range(len(res)):
			if i + 1 < len(res) and res[i] == p:
				return res[i + 1]

		return None

# time: O(n)
# space: O(n)


if __name__ == '__main__':
	s = Solution()
	root = TreeNode(5)
	root.left = TreeNode(3)
	root.right = TreeNode(6)
	root.right.right = TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, val=0, left=None, right=None):
	#         self.val = val
	#         self.left = left
	#         self.right = right
	class Solution:
		def flatten_optimal_space(self, root: Optional[TreeNode]) -> None:
			"""
			Do not return anything, modify root in-place instead.
			"""
			# While traversing, for every node, check whether it has a left child or not. If the left child does not exist, move on to the right child. Otherwise, find the node on the rightmost branch of the left subtree which does not have a right child. Once this rightmost node is found, connect it with the right child of the current node. After connecting, set the right child of the current node to the left child of the current node. Finally, set the left child of the current node to NULL.
			if not root:
				return
			current = root
			while current:
				if current.left:
					last = current.left

					while last.right:
						last = last.right

					last.right = current.right
					current.right = current.left
					current.left = None

				current = current.right

	# time: O(n), n is total nodes in the BT
	# space: O(1)

	def flatten_iterative(self, root: Optional[TreeNode]) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		if not root:
			return

		stack = [root]

		while stack:
			node = stack.pop()
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

			if stack:
				node.left = None
				node.right = stack[-1]
			else:
				node.left = None


# time = space = O(n), n is the number of nodes in the BT


def flatten_recursive(self, root: Optional[TreeNode]) -> None:
	"""
	Do not return anything, modify root in-place instead.
	"""
	"""
	- The idea is that for a current node, we have to flatten all the nodes in its left node first and connect the left tail of the left subtree with the current's right node.  
	"""

	def helper(node: TreeNode) -> TreeNode:
		if not node:
			return None
		# for a leaf nodem, we simply return the node as is
		if not node.left and not node.right:
			return node

		left_tail = helper(node.left)
		right_tail = helper(node.right)

		# if there was a left subtree, we update the connnection
		if left_tail:
			left_tail.right = node.right
			node.right = node.left
			node.left = None

		return right_tail if right_tail else left_tail

	helper(root)

# time: O(n), n is the number of nodes in the BT
# space: O(n)

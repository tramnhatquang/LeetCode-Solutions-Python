from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator_1:

	def __init__(self, root: TreeNode):

		# Stack for the recursion simulation
		self.stack = []

		# Remember that the algorithm starts with a call to the helper function
		# with the root node as the input
		self._leftmost_inorder(root)

	def _leftmost_inorder(self, root):

		# For a given node, add all the elements in the leftmost branch of the tree
		# under it to the stack.
		while root:
			self.stack.append(root)
			root = root.left

	def next(self) -> int:
		"""
		@return the next smallest number
		"""

		# Node at the top of the stack is the next smallest element
		topmost_node = self.stack.pop()

		# Need to maintain the invariant. If the node has a right child, call the
		# helper function for the right child
		if topmost_node.right:
			self._leftmost_inorder(topmost_node.right)
		return topmost_node.val

	def hasNext(self) -> bool:
		"""
		@return whether we have a next smallest number
		"""
		return len(self.stack) > 0


class BSTIterator:

	def __init__(self, root: Optional[TreeNode]):
		self.sorted_arr = []
		# pointer to the next smallest element in the BST
		self.index = 0

		# call the flatten the input BST
		self._inorder(root)

	# time = space =O(n)

	def _inorder(self, root):
		if root:
			self._inorder(root.left)
			self.sorted_arr.append(root.val)
			self._inorder(root.right)

	def next(self) -> int:
		temp = self.index
		self.index += 1
		return self.sorted_arr[temp]

	# time: O(1) ,space = O(n)

	def hasNext(self) -> bool:
		return self.index < len(self.sorted_arr)
# time = O(1), space: O(n)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

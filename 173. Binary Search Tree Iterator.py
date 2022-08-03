from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class BSTIterator:

	def __init__(self, root: Optional[TreeNode]):
		self.sorted_arr = []
		# pointer to the next smallest element in the BST
		self.index = 0

		# call the flatten the input BST
		self._inorder(root)

	def _inorder(self, root):
		if root:
			self._inorder(root.left)
			self.sorted_arr.append(root.val)
			self._inorder(root.right)

	def next(self) -> int:
		temp = self.index
		self.index += 1
		return self.sorted_arr[temp]

	def hasNext(self) -> bool:
		return self.index < len(self.sorted_arr)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

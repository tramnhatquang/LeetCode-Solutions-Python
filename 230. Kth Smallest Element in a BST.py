# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		# Approach 1: Store all the values into a min heap
		# return the k-th smallest value is equivalent to return heapq.nsmallest(k)[-1]

		#         res = []
		#         def dfs(root: TreeNode) -> None:
		#             if root:
		#                 res.append(root.val)
		#                 dfs(root.left)
		#                 dfs(root.right)
		#         dfs(root) # O(n)
		#         print(res)

		#         heapq.heapify(res) #O(n)
		#         return heapq.nsmallest(k, res)[-1] # O(log k)

		# time: O(n + logK), space: O(n), n is the total nodes in the binary search tree

		# approach 2: Inorder traversal.
		# inorder traversal gives us a sorted order of all nodes' values
		# the k-th smallest value is the (k - 1) index

		# inorder traversal: visit root -> visit left subtree -> visit right subtree
		# def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

		# res = []
		# def inorder(root: TreeNode) -> List[int]:
		#     if root:
		#         inorder(root.left)
		#         res.append(root.val)
		#         inorder(root.right)
		# inorder(root)
		# return res[k - 1]

		# time = space = O(n)

		# APPROACH 3: Iterative approach using inorder traversal
		stack = []
		while root or stack:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			k -= 1
			if k == 0:
				return root.val
			root = root.right

	# time: O(H + k) where H is the tree height,
	# space: O(H) to keep the stack, where H is a tree height. That makes O(N) in the worst case of the skewed tree, and O (log N ) in the average case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		# solve this problem using iteration

		if not root:
			return None

		curr = root
		while curr:

			# traversely look for the left subtree
			if curr.val > p.val and curr.val > q.val:
				curr = curr.left
			elif curr.val < p.val and curr.val < q.val:
				curr = curr.right
			else:
				# now we found the split point (LCA node)
				return curr

	# time = space = O(n)
	def lowestCommonAncestor_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		# find the lowest common node where p and q are descendants
		# the lowest common ancestor is also the lowest common split node between p and q

		# recursively traverse to the right
		if p.val > root.val and q.val > root.val:
			return self.lowestCommonAncestor(root.right, p, q)
		elif p.val < root.val and q.val < root.val:
			# recursively traverse to the left
			return self.lowestCommonAncestor(root.left, p, q)

		# root is the split point
		return root
# time = O(n), space = O(n)

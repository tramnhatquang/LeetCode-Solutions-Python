# User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# your task is to complete this function

class Solution:
	# Function to convert a binary tree into its mirror tree.
	def mirror_recursive(self, root):
		# Code here
		# base case
		if not root:
			return

		self.mirror(root.left)
		self.mirror(root.right)

		# swapping
		temp = root.left
		root.left = root.right
		root.right = temp

	# time = space = O(n)

	def mirror_iterative(self, root):
		# Code here

		# solve using iterative approach
		if not root:
			return

		queue = deque([root])
		while queue:
			curr_length = len(queue)

			for _ in range(curr_length):
				node = queue.popleft()
				# swap left child with right child
				node.left, node.right = node.right, node.left
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

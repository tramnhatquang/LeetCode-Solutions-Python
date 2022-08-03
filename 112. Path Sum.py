# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
		# approach 1: DFS + stack
		# each state contains the curr sum starting from the root
		# time: O(n), n is total nodes in the BT
		# space: O(n)
		#         if not root:
		#             return False

		#         stack = [(root, root.val)]
		#         while stack:
		#             curr, curr_sum = stack.pop()
		#             # check if we have reached a leaf node
		#             if not curr.left and not curr.right and curr_sum == targetSum:
		#                 return True
		#             if curr.left:
		#                 stack.append((curr.left, curr.left.val + curr_sum))
		#             if curr.right:
		#                 stack.append((curr.right, curr.right.val + curr_sum))
		#         return False # there is not path in the binary tree

		# approach 2: DFS + stack
		# current state is the node itself and the remaining_sum after deducting the current node's value
		# if we reach a leaf node and the reamining sum  == 0, we return True
		# time = space = O(n)
		#         if not root:
		#             return False
		#         stack = [(root, targetSum - root.val)]
		#         while stack:
		#             node, curr_sum = stack.pop()
		#             if not node.left and not node.right and curr_sum == 0:
		#                 return True
		#             if node.right:
		#                 stack.append((node.right, curr_sum - node.right.val))
		#             if node.left:
		#                 stack.append((node.left, curr_sum - node.left.val))

		#         return False

		# approach 3: Recursion + DFS
		# time = space = O(n)
		#         if not root: # our base case
		#             return False

		#         targetSum -= root.val
		#         if not root.left and not root.right and targetSum == 0:
		#             return True
		#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

		# approach 4: BFS + queue
		# time = space = O(n)
		if not root:
			return False
		queue = [(root, targetSum - root.val)]
		while queue:
			curr, val = queue.pop(0)
			if not curr.left and not curr.right and val == 0:
				return True
			if curr.left:
				queue.append((curr.left, val - curr.left.val))
			if curr.right:
				queue.append((curr.right, val - curr.right.val))
		return False

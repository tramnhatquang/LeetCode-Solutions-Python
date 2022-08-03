# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
	#         # approach 1: Using two DFS to walk through any poosible nodes downward and calculate the sum of each path. If the path is equal to targetSum, increase the count by 1. We use a global variable counter to keep track of

	#         self.num_paths = 0
	#         self.dfs1(root, targetSum)
	#         return self.num_paths

	#     # traverse through each node, and treat each new node as a root node and find different paths from the current node
	#     def dfs1(self, root: TreeNode, target: int) -> None:
	#         if not root: # base case
	#             return

	#         self.dfs2(root, target)
	#         self.dfs1(root.left, target)
	#         self.dfs1(root.right, target)

	#      # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
	#     def dfs2(self, root:TreeNode, target: int) -> None:
	#         if not root:
	#             return
	#         target -= root.val
	#         if target == 0:
	#             self.num_paths += 1

	#         self.dfs2(root.left, target)
	#         self.dfs2(root.right, target)

	# time: O(n log n) -> O(n^2) due to the double DFS recursive calls
	# space: O(n) due to the call stack

	# approach 2: Using prefix sum technique to reduce the TC

	# we use a hash map to keep thr occurences of prefix sum we have walked past so far
	# At any node we are at, we check if the current prefix sum equals to the target, if is does, we increment the count by 1 (count += 1). However, the tree path with the target sum starts somewhere downwards. That means we should add to the counter the number of times we have seen the prefix sum curr_sum - target so far: count += h[curr_sum - target].
	def pathSum(self, root: TreeNode, target: int) -> int:
		# define a global variable to keep track of the number of paths
		self.num_paths = 0
		self.hash_map = {}

		# call the DFS
		self.dfs(root, target, 0)
		return self.num_paths

	def dfs(self, root: TreeNode, target: int, curr_sum: int) -> None:
		if not root:
			return

		curr_sum += root.val
		if curr_sum == target:
			self.num_paths += 1

		if (curr_sum - target) in self.hash_map:
			self.num_paths += self.hash_map[curr_sum - target]

		if curr_sum in self.hash_map:
			self.hash_map[curr_sum] += 1
		else:
			self.hash_map[curr_sum] = 1

		self.dfs(root.left, target, curr_sum)
		self.dfs(root.right, target, curr_sum)

		self.hash_map[curr_sum] -= 1

# time: O(n)
# space: O(n)

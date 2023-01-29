# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

	def binaryTreePaths_dfs_iterative(self, root: Optional[TreeNode]) -> List[str]:

		if not root:
			return []

		ans = []
		stack = [(root, str(root.val))]
		while stack:
			node, path = stack.pop()
			if not node.left and not node.right:
				ans.append(path)
			if node.left:
				stack.append((node.left, path + "->" + str(node.left.val)))
			if node.right:
				stack.append((node.right, path + "->" + str(node.right.val)))

		return ans


def binaryTreePaths_dfs_recursive(self, root: Optional[TreeNode]) -> List[str]:
	res = []

	def dfs(root: ListNode, curr_path: List[int]) -> None:

		if not root:
			return

		curr_path.append(str(root.val))

		# check if we reach a leaf node
		if not root.left and not root.right:
			res.append('->'.join(curr_path))
			return

		# append the curr node into the curr_path
		if root.left:
			dfs(root.left, curr_path)
			curr_path.pop()  # backtracking
		if root.right:
			dfs(root.right, curr_path)
			curr_path.pop()  # backtracking

	dfs(root, [])
	return res
# time: O(n) = space

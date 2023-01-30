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

		def dfs(node: ListNode, path: List[str]) -> None:
			# base case
			if not node:
				return

			path.append(str(node.val))

			# check if we reach a leaf node
			if not node.left and not node.right:
				res.append('->'.join(path))
				path.pop()
				return

			dfs(node.left, path)
			dfs(node.right, path)
			path.pop()

		dfs(root, [])
		return res


# time: O(n) = space

if __name__ == '__main__':
	s = Solution()

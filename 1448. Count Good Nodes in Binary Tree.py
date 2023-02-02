
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes_dfs_iterative(self, root: TreeNode) -> int:
        # solve it with iterative approach
        # dfs
        stack = [(root, float('-inf'))]
        count = 0
        while stack:
            node, maxValue = stack.pop()
            if node and node.val >= maxValue:
                count += 1
            if node.left:
                stack.append((node.left, max(node.val, maxValue)))
            if node.right:
                stack.append((node.right, max(node.val, maxValue)))

        return count

    def goodNodes_recursive(self, root: TreeNode) -> int:
        # DFS, recursive
        count = 0

        def dfs(node: TreeNode, maxVal: float) -> None:
            nonlocal count
            if not node:
                return

            if node.val >= maxVal:
                count += 1

            dfs(node.left, max(node.val, maxVal))
            dfs(node.right, max(node.val, maxVal))

        dfs(root, float('-inf'))
        return count

        # time = space = O(n)

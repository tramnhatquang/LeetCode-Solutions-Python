# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves_recursive_1(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves_recursive_1(root.left) + self.sumOfLeftLeaves_recursive_1(root.right)

    def sumOfLeftLeaves_recursive_2(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode, is_left: bool) -> int:
            if not node:  # base case
                return 0
            # check if we have left leaf node
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)

    def sumOfLeftLeaves_iterative_approach(self, root: Optional[TreeNode]) -> int:
        """
        Observation: We cannot consider the root as a left leaf node. A left leaf node is a leaf thast is the left child of another node
        """

        if not root:
            return 0
        total = 0
        stack = [
            (root, False)]  # we store a node and the bool value indicating if the node is a left node of a parent node
        while stack:
            node, is_left = stack.pop()
            if not node.left and not node.right and is_left:
                total += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))

        return total

        # time = O(n) = space, n is total nodes in the binary tree

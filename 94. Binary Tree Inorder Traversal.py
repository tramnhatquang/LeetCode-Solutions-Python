from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        while stack or root:
            # traverse all the way to left
            while root:
                stack.append(root)
                root = root.left

            # pop out from the top of the stack and append it the result arr
            root = stack.pop()
            res.append(root.data)
            root = root.right

        return res

    # time = space = O(n)

    def inorderTraversal_recursive_1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        return self.inorderTraversal(root.left) + [
            root.val] + self.inorderTraversal(root.right)

    def inorderTraversal_recursive_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        return '{} {} {}'.format(root.val, self.serialize(root.left),
                                 self.serialize(root.right))


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    s = Solution()
    print(s.serialize(root))

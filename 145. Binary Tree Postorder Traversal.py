# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        # do the same iterative approach of the preorder approach but in the reverse order
        if not root:
            return []

        res, stack = [], [root]
        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return res[::-1]
        # time = space = O(n)

    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def helper(root, arr):
            if not root:
                return
            helper(root.left, arr)
            helper(root.right, arr)
            arr.append(root.val)

        helper(root, arr)
        return arr

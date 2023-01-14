# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        # code here
        # visit root -> left subtree -> right subtree
        res = []

        def helper(root):
            if root:
                res.append(root.data)
                helper(root.left)
                helper(root.right)

        helper(root)
        return res

    def preorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        # return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        if not root:
            return []  # an empty list if the root node is Null

        res, stack = [], [root]
        while stack:
            root = stack.pop()
            res.append(root.val)

            # append node into the stack (root.right first then root.left)
            # since we need to process the left nodes before the right nodes
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tree2str_approach_3(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        elif not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        else:
            return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"

    def tree2str_approach_2(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(node: TreeNode) -> None:
            if not node:
                return
            res.append(str(node.val))
            # check if left node is None and right node is NOT None
            if not node.left and not node.right:
                return
            res.append("(")
            preorder(node.left)
            res.append(")")

            if node.right:
                res.append("(")
                preorder(node.right)
                res.append(")")

        preorder(root)
        return ''.join(res)

        # time = space = O(n)

    def tree2str_approach_1(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(node: TreeNode) -> None:
            if not node:
                return

            res.append("(")
            res.append(str(node.val))
            # check if left node is None and right node is NOT None
            if not node.left and node.right:
                res.append("()")
            # ex: 1(2()(4))(3)

            preorder(node.left)
            preorder(node.right)
            res.append(")")

        preorder(root)
        return ''.join(res[1:-1])

        # time = space = O(n)

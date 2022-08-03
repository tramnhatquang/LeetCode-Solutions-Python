# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n) where n is the number of nodes
    # Space: O(h) where h is the height of the tree
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.checkUni(root, None)
        return self.ans

    def checkUni(self, root, parent) -> bool:
        if not root:
            return True

        left = self.checkUni(root.left, root.val)
        right = self.checkUni(root.right, root.val)
        if left and right:
            self.ans += 1
        return left and right and root.val == parent


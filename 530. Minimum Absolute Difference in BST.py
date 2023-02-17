# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_val = float('inf')
        self.prev_node = None

        def inorder(node: TreeNode) -> None:
            if node:
                inorder(node.left)
                if self.prev_node:
                    # update the min value
                    self.min_val = min(self.min_val, abs(self.prev_node.val - node.val))
                # update the prev node
                self.prev_node = node
                inorder(node.right)
        inorder(root)
        return self.min_val 

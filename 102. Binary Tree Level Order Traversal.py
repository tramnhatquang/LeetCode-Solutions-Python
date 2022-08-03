# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            levels = []

            def helper(node, level):
                if node:
                    if len(levels) == level:
                        levels.append([])
                    levels[level] += [node.val]
                    helper(node.left, level + 1)
                    helper(node.right, level + 1)

            helper(root, 0)
            return levels

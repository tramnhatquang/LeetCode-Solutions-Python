# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = root.val

        def dfs(node: ListNode) -> int:
            nonlocal max_val
            """
            Return the max path sum starting from the node
            """
            # base case
            if not node:
                return 0

            # find the max path sum from the left and right subtrees
            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            # compute the max so far with the split
            max_val = max(max_val, node.val + leftMax + rightMax)

            # return the max sum for a path starting at the root of subtree
            return max(leftMax + node.val, rightMax + node.val)

        dfs(root)
        return max_val

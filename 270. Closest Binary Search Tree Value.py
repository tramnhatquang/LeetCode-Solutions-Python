# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *

class Solution:

    def closestValue_optimal(self, root: Optional[TreeNode], target: float) -> int:
        # Basically, we do not need to store all the calculations and differences and then compare
        # We can optimize the time complexity to O(h) where h is the height of the tree, and O(1) for space complexity
        # Basically, we want to go the nearest node value to the target
        min_val = root.val
        while root:
            if abs(root.val - target) < abs(min_val - target):
                min_val = root.val
            elif root.val < target:
                root = root.right
            else:
                root = root.left
        return min_val

        # time: O(H) = O(log n), H is height of BST
        # spacE: O(1)

    def closestValue_brute_force(self, root: Optional[TreeNode], target: float) -> int:
        res = []
        # loop thr each node in the BST and store both the (node.val, diff) into the arr
        # after that, we traverse thr the arr and find the min_val
        def dfs(node: TreeNode, target: int) -> None:
            if not node:
                return

            res.append((node.val, abs(target - node.val)))
            dfs(node.left, target)
            dfs(node.right, target)

        dfs(root, target)
        min_diff = float('inf')
        min_val = -1
        for val, diff in res:
            if diff < min_diff:
                min_diff = diff
                min_val = val
        return min_val

        # time = space = O(n)
        # the question is can we optimize the solution and do not use the extra arr to store the diff

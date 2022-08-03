from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Recursive approach:
        # Time: O(n)
        # Space: O(n) because the recursive calls are bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n)O(n)
        return not root or self.helper_symmetric(root.left, root.right)

    def helper_symmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.helper_symmetric(left.left, right.right) and self.helper_symmetric(left.right, right.left)

        # iterative approach: Using a queue
        # Time: O(n)
        # Space: O(n)
        if not root:
            return True
        q = []
        q.append(root.left);
        q.append(root.right);
        while q:
            left = q.pop(0)
            right = q.pop(0)
            if not left and not right:
                continue;
            if not left or not right:
                return False;
            if left.val != right.val:
                return False
            q.append(left.left);
            q.append(right.right);
            q.append(left.right);
            q.append(right.left);
        return True;













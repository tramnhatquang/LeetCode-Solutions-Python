from typing import List, Optional, Tuple, Union
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return TreeNode(val)

        if root.val < val:
            # insert into the right subtree
            root.right = self.insertIntoBST_recursive(root.right, val)
        else:
            root.left = self.insertIntoBST_recursive(root.left, val)

        return root

    # time = O(N), space: O(h) where h is the height of the tree

    def insertIntoBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # iterative approach
        if not root:
            root = TreeNode(val)
            return root

        curr = root
        while curr:
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left

        curr = TreeNode(val)
        return root

# time = O(N), space: O(h) where h is the height of the tree

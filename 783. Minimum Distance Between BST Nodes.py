# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyparsing import Optional


class Solution:
def minDiffInBST_optimal(self, root: Optional[TreeNode]) -> int:
        """
        While traversing thr the BST inorder traversal, we can keep track of the min_diff so far, we can save some space complexity
        """
        self.min_diff = float('inf')
        self.prev_node = None # keep track of the prev node in the inorder traversal
        def inorder(node: TreeNode) -> None:
            if node:
                inorder(node.left)
                if self.prev_node:
                    self.min_diff = min(self.min_diff, abs(self.prev_node.val - node.val))
                self.prev_node = node
                inorder(node.right)

        inorder(root)
        return self.min_diff
        # time: O(n) n is the number of nodes
        # spacE: O(H), h is the height of the tree. In the worst case scenario, H == N
    
    
    def minDiffInBST_using_list(self, root: Optional[TreeNode]) -> int:
        """
        Since we want to find the min difference between every node in a binary search tree. We can think of how to find the min difference in a sorted arr. 
            - We do not need to find the min diff between every possible pairs. We just need to find the min diff between consecutive pairs
        """
        sorted_lst = []
        def inorder(node: TreeNode) -> None:
            if node:
                inorder(node.left)
                sorted_lst.append(node.val)
                inorder(node.right)
        inorder(root)
        min_diff = float('inf')
        for i in range(len(sorted_lst) - 1):
            min_diff = min(min_diff, abs(sorted_lst[i] - sorted_lst[i + 1]))
 
        return min_diff
        # time: O(n) = space, n is the number of nodes

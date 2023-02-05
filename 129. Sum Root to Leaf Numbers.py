# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    
    def sumNumbers_appr_1(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # we use global variables to keep track of all the root-to-leaf paths


        def dfs(node: TreeNode, curr_num: int) -> None:
            nonlocal ans
            # base case
            if not node:
                return

            # build the number before going to its subtrees
            curr_num = curr_num * 10 + node.val
            # if we reach a leaf node, we add the curr_num into the answer
            if not node.left and not node.right:
                ans += curr_num
                return

            dfs(node.left, curr_num)
            dfs(node.right, curr_num)

        dfs(root, 0)
        return ans
        # time = O(n) = space

        """
        Do some dry runs
            1
           2  3

        dfs(1) -> curr_num = 1 
            dfs(2, 1) -> curr_num = 12 
                dfs(None)
                dfs(None)
            dfs(3, 1) -> curr_num = 13
                dfs(None)
                dfs(None)
        ans = 25
        """

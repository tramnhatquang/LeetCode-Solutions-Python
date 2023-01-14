class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        if root == p or root == q:
            return root
        # we recursively look for both nodes in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right  # if one of subtree is None, we cannot find both nodes in that subtree, and we just return the one that is not null
        # Time: O(n)
        # Space: O(n)

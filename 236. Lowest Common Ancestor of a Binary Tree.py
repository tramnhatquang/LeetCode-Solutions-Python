def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                         q: 'TreeNode') -> 'TreeNode':
    # Time: O(n)
    # Space: O(n)
    if not root:
        return None
    if root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if not left and not right:
        return None
    if left and right:
        return root
    return right if not left else left

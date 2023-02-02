# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree_approach_1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the first value in the preorder is ALWAYS the root node of the new constructed binary tree
        # all the values to the left of the root's value in the INORDER traversal belong to its left subtree. Similarly, all the values to the right of the root's value belong to its right subtree
        if not preorder or not inorder:
            return None

        # we can think about using recursion to solve this problem
        root = TreeNode(preorder[0])

        # find the index of root in the inorder traversal
        mid = inorder.index(preorder[0])
        # recursively build the left subtree
        root.left = self.buildTree_1(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree_1(preorder[mid + 1:], inorder[mid + 1:])
        return root

        # time = O(n)  = space , n is length of arr
        
        
    def buildTree_approach_2(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right:
                return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(
                inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
		# store the sorted LL into an arr
		res = []
		curr = head
		while curr:
			res.append(curr.val)
			curr = curr.next

		# to make a height-balanced BST, we need to take the middle val as the root node's val and all values in the left side of middle value belong to the all left nodes of the root. Similarly, all right values belong to the all right nodes of the root
		n = len(res)

		def build_tree(left: int, right: int) -> TreeNode | None:
			if left > right:  # invalid cases
				return None

			mid = (left + right) // 2
			node = TreeNode(res[mid])
			if left == right:
				return node
			node.left = build_tree(left, mid - 1)
			node.right = build_tree(mid + 1, right)
			return node

		return build_tree(0, n - 1)

# time: O(N), N is total nodes in the BST
# space: O(N) due to the arr construction

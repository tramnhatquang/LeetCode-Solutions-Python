from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# approach 1: Iterative in-place reverse
		# For a current node, we need to keep track of the next nodes's reference by using an pointer to store that reference. We link the current node's next to the previous node. Meaning that we also keep track of the reference of the prev node.
		# After that, we move the current to the next node, and the prev node to the current node. By the time the current node is None, the previous is the new head of the reversed LL

		# time: O(n), n is the number of nodes in the LL
		# space: O(1)
		# prev, curr = None, head
		# while curr:
		#     next_node = curr.next
		#     curr.next = prev
		#     prev = curr
		#     curr = next_node
		# # prev is the new head of reversed LL
		# return prev

		# approach 2: Recursion
		# the base case (when we have no nodes or only one node)
		if not head or not head.next:
			return head

		# the result of this function returns the new_head of the linked list
		new_head = self.reverseList(head.next)

		# 1-> 2 -> 3 -> N
		#    curr
		#  How do we update the current node's next so that 1 -> 2 <- 3
		head.next.next = head
		head.next = None

		return new_head

# Time: O(n), space: O(n)

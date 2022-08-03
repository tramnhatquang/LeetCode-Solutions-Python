from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> \
			Optional[ListNode]:
		# approach 1: Iteration + One pass
		# 1. traverse to the (left - 1)-th node so that we can link (left-1)th to the end of reversed sub-list at the end
		# 2. Keep track of the head of the sub-list since it is the last node of the sublist after reversing
		# 3. Use a sentinel head to keep track of the head' reference in case the reversed sub-list includes the head
		# 4. if we start from the sentinel head with a prev variable. After (left - 1) step, we advance the prev variable by 1 step and it will point to the (left- 1) node. Assign a current variable to prev.next which is the (left) node from the start. We will reverse all nodes between left and right.
		#             if not head or left == right: # the LL is unchanged
		#                 return head

		#             sentinel = prev = ListNode(0, head)
		#             for _ in range(left - 1):
		#                 prev = prev.next

		#             # the left node is prev.next
		#             last_node_first_part = prev
		#             curr = prev.next
		#             last_node_sub_list = curr
		#             for _ in range(right - left + 1):
		#                 nxt = curr.next
		#                 curr.next = prev
		#                 prev = curr
		#                 curr = nxt

		#             # at here, the curr node points to the (right + 1) node
		#             # prev is the head of the reversed sub-list
		#             last_node_first_part.next = prev
		#             last_node_sub_list.next = curr

		#             return sentinel.next

		# time: O(n), O(1) for space, N is the length of the LL
		# approach 2: we can shorten the code a little bit while reversing and connecting the head of reversed sub-list to the last node of the first part
		if not head or left == right:  # the LL is unchanged
			return head

		sentinel = prev = ListNode(0, head)
		for _ in range(left - 1):
			prev = prev.next

		curr = prev.next
		for _ in range(right - left):
			temp = curr.next
			curr.next = temp.next
			temp.next = prev.next
			prev.next = temp

		return sentinel.next

	# time: O(n), spacE: O(1) but the second while loop is quite complicated and easy to mess up all the links

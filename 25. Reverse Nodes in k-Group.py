from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

		# create a sentinel head, helps us to keep track of the head of the LL when we reverse
		sentinel = group_previous = ListNode(0, head)

		#  start reversing
		while True:
			kth_node = self.get_kth(group_previous, k)
			# when the k-th node is None, we have less than k nodes left to reverse
			if not kth_node:
				break

			group_next = kth_node.next
			# reverse group
			prev, curr = kth_node.next, group_previous.next
			while curr != group_next:
				nxt = curr.next
				curr.next = prev
				prev = curr
				curr = nxt

			# link the previous reversed group to the next group
			temp = group_previous.next
			group_previous.next = kth_node
			group_previous = temp

		return sentinel.next

	def get_kth(self, curr: ListNode, k: int) -> ListNode:
		while curr and k > 0:
			curr = curr.next
			k -= 1
		return curr

# TIme: O(n), space: O(1)

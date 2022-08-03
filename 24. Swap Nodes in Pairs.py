# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def swapPairs(self, head: ListNode) -> ListNode:
		# APPROACH 1: Sentinel Head + swap in paris
		# We will use the sentinel node to keep track pf the reference to the head node

		# Check if there is only one node or not any nodes in the LL
		if not head or not head.next:
			return head

		# At here, there are at least two nodes
		sentinel = prev = ListNode(0, head)

		# check if we have a pair to swap
		while head and head.next:
			# two nodes to be swapped
			first = head
			second = head.next

			# Swapping
			# After swapping, the first node turns to be the second node while the second node is the first node in the current pair
			prev.next = second
			first.next = second.next
			second.next = first

			# move on to the next pairs
			head = first.next
			prev = first

		return sentinel.next

# time: O(N), N is the length of the LL

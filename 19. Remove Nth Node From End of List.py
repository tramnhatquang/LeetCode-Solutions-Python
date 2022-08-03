from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[
		ListNode]:
		# approach 1: Count the length of the linked list and remove the n-th
		# node starting from the end of LL if the length of LL is m, then the
		# n-th node from the end of the list is (m - n + 1)-th node from the
		# start. We will find the length of LL first then traverse to the (m -
		# n)-th node (the node before the removed node). After that, we change
		# (m - n)-th node's next to the next 's next node

		# use the dummy node to handle the edge case when ( n== m, we need to
		# remove the head node) dummy = ListNode(0, head) length = 0 curr =
		# head while curr: length += 1 curr = curr.next

		#         length -= n
		#         curr = dummy
		#         for _ in range(length):
		#             curr = curr.next

		#         # update the link of the node just right before the removed node
		#         curr.next = curr.next.next
		#         return dummy.next

		# time: O(n), n is total nodes in the LL
		# space: O(1), only use constant space

		# approach 2: Use only one pass
		dummy = ListNode(0, head)
		slow = fast = dummy
		# move the fast pointer so that the gap between the slow and fast pointer is n nodes apart
		for _ in range(n + 1):
			fast = fast.next
		# move two pointer simultaneously to the end of LL
		while fast:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next
		return dummy.next

	# time: O(n), space: O(1)

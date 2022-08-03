from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		slow = fast = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				break
		else:
			return None
		while head != slow:
			head, slow = head.next, slow.next

		return slow

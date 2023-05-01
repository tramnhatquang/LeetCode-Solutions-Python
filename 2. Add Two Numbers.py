from typing import *

from Utilities.ListNode import ListNode


# Definition for singly-linked list.

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
			Optional[ListNode]:
		# Time: O(max(n, m))
		# Space: O(max(n, m))
		# write your code below here
		dummy = cur = ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			cur.next = ListNode(carry % 10)
			cur = cur.next
			carry //= 10
		return dummy.next

from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode],
	                  list2: Optional[ListNode]) -> Optional[ListNode]:
		# approach: TWO POINTERS (ONLY FOR TWO SORTED LL)
		# EACH POINTER POINTS TO THE HEAD OF EACH LL, IF ONE OF THE POINTER'S VALUE IS LESS THAN THE OTHER'S, YOU LINK THE CCURR NODE'NEXT TO THAT NODE, AND MOVE BOTH THE CURR POINTER AND P1 AHEAD. OTHERWISE, YOU MOVE P2 AND CURRENT NODE

		# KEEP DOING THAT UNTIL ONE OF THE POINTER IS NONE
		# WE LINK THE CURR NODE 'S NEXT TO WHAT 'S LEFT IN THE NON-NONE POINTER

		#         p1, p2 = list1, list2
		#         # keep track of the head node
		#         sentinel = curr =  ListNode(0)

		#         while p1 and p2:
		#             if p1.val < p2.val:
		#                 curr.next = p1
		#                 p1 = p1.next
		#             else:
		#                 curr.next = p2
		#                 p2 = p2.next

		#             curr = curr.next

		#         # link the current node's next to what's left from the non-none pointer
		#         curr.next = p1 or p2
		#         return sentinel.next

		# time: O(n), space: O(1), n is the number of nodes in the LL

		# approach 2: Recursion
		# the base cases
		if not list1:
			return list2
		elif not list2:
			return list1

		# make recursive calls
		if list1.val < list2.val:
			list1.next = self.mergeTwoLists(list1.next, list2)
			return list1
		else:
			list2.next = self.mergeTwoLists(list1, list2.next)
			return list2
# time = space = O(n)

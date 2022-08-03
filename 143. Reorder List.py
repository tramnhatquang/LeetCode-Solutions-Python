from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""

		# check if we only have one node or not any nodes:
		if not head or not head.next:
			return

		# Algorithm:
		# 1. FInd the middle node of the LL. If the LL is odd, the middle node is the node in the middle. If the LL is even, the middle node is the second middle node in the LL.
		# 2. Reverse the second half of the LL, including the middle node
		# 3. Have two pointers, one points to the head, while the second one points to the middle node. Two pointers will move simutaneously and link to each other. We continue to do it until the second pointer's next is Null

		# find the middle node
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# slow pointer points to the middle node
		head_second_half = self.reverse(slow)
		first, second = head, head_second_half
		while second.next:
			first.next, first = second, first.next
			second.next, second = first, second.next

	# while first and second:
	# 	temp = first.next
	# 	first.next = second
	# 	first = temp
	#
	# 	temp = second.next
	# 	second.next = first
	# 	second = temp
	#
	# if not first:
	# 	first.next = None
	# time: O(N), N is the length of LL
	# space: O(1)

	def reverse(self, head: ListNode) -> ListNode:
		prev, curr = None, head
		while curr:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node

		return prev

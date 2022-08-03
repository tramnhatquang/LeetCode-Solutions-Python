# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		# APPROACH 1:
		# 1. Using a pointer pointing at the head of the linked list
		# 2. If the next node's value equals to the current node's val,
		# update the next node to the next.next
		# curret.next = current.next.next
		# Repeat step 2 if the next node's value is still equal to current node's value
		# 3. Otherwise, we move the pointer a head by 1
		# Reapeat step 1, 2, 3 until we reach the end of the linked list

		pointer = head
		while pointer and pointer.next:
			if pointer.val == pointer.next.val:
				pointer.next = pointer.next.next
			else:
				pointer = pointer.next

		return head

# time: O(n), space: O(1), where N is the length of LL

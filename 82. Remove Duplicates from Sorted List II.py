# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# APPROACH 1: Using a sentinel head + predecessor
		prev = dummy = ListNode(0, head)

		# move the head pointer if the next value is equal to the current value
		while head and head.next:
			if head.val == head.next.val:
				while head.next and head.val == head.next.val:
					head = head.next
				# head will point to the last element in the duplicate sequence
				head = head.next
				# connect the prev's next to the head
				prev.next = head

			else:
				prev = prev.next
				head = head.next
		return dummy.next

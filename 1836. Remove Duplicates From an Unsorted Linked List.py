# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

		# keep track of all the occurences of values in the LL
		freq_table = collections.Counter()
		curr = head
		while curr:
			freq_table[curr.val] += 1
			curr = curr.next

		# start with a sentinel head pointing to the head and a prev node keeps tracks of the predessor node before the current node
		# if the current nodes' value occurs more than once, we link the prev node's next to the current node's next and move the current node by 1. Otherwise, we move both the current and previous node a head by 1

		dummy = prev = ListNode(0, head)
		while head:
			if freq_table[head.val] > 1:
				prev.next = head.next
			else:
				prev = prev.next

			head = head.next
		return dummy.next

	# time: O(n), space: O(n) where N is the length of LL
	# in the worst case scenario, the hash map contains all the distinct values from the LL

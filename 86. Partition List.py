# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
		# approach: two pointers approach
		# 1. Create two sentinels head .One stores all the nodes whose values are less than x. Second one stores all the nodes whose values are larger than or equal to x. We need to keep track of both the tails of two newly created LL so that we can link the tail of left to the head of the right LL

		left, right = ListNode(), ListNode()
		left_tail, right_tail = left, right

		# loop over the main LL
		while head:
			# connect to the left LL if the current value is less than x
			if head.val < x:
				left_tail.next = head
				left_tail = left_tail.next
			# connect to the right LL if the current value is greater than or equal to x
			else:
				right_tail.next = head
				right_tail = right_tail.next

			head = head.next
		# connect the left_tail to head of the right LL
		left_tail.next = right.next
		right_tail.next = None

		return left.next

# time: O(n), space: O(1)

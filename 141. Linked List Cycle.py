from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		# approach 1: Use a hash set to store the visited nodes. When we traverse to a node which had been visited before, we return True. Otherwise, after reaching the end of the LL, we do not find any duplicate node then we returns False
		# visited = set()
		# curr = head
		# while curr:
		#     if curr in visited:
		#         return True
		#     visited.add(curr)
		#     curr = curr.next
		# return False

		# time: O(n) = space, n is the number of nodes in the LL

		# approach 2: Use fast, slow pointers
		# Fast and slow pointers both start at the head. Move the fast pointer 2 steps and slow pointer one step at a time. After some iterations, the fast pointer catches up with the slow pointer. The reason is that if the fast pointer jumps over the slow pointer , the slow pointer is equal to the fast pointer in the next step
		slow = fast = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				return True

		return False

# time: O(n), space: O(1)

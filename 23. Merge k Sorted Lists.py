from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[
		ListNode]:
		# approach 1: Brute force solution
		# Traverse all the linked lists and collect the values of the nodes into an array.
		# Sort and iterate over this array to get the proper value of nodes.
		# Create a new sorted linked list and extend it with the new nodes.

		#         self.nodes = []
		#         # Create a sentinel head to keep track of the head's reference
		#         sentinel = curr = ListNode()
		#         for l in lists:
		#             while l:
		#                 self.nodes.append(l.val)
		#                 l = l.next

		#         for element in sorted(self.nodes):
		#             curr.next = ListNode(element)
		#             curr = curr.next

		#         return sentinel.next

		# time: O(N log N), N is total number of nodes
		#   -Collecting all the values costs O(N)O(N) time.
		#   -A stable sorting algorithm costs O(N\log N)O(NlogN) time.
		#   -Iterating for creating the linked list costs O(N)O(N) time.

		# space: O(n) based on the built-in sort

		# approach 2: Merge with Divide and Conquer
		#   - Pair up k lists and merge each pair.
		#   - After the first pairing, \text{k}k lists are merged into k/2k/2 lists with average 2N/k2N/k length, then k/4k/4, k/8k/8 and so on.
		#   -Repeat this procedure until we get the final sorted linked list.
		if not lists:
			return None
		# merge each pair of two lists
		while len(lists) > 1:
			mergedList = []

			for i in range(0, len(lists), 2):
				list1 = lists[i]
				list2 = lists[i + 1] if (i + 1) < len(lists) else None
				mergedList.append(self.mergeList(list1, list2))
			lists = mergedList

		return lists[0]

	# implementation of merge two sorted LL
	def mergeList(self, list1, list2):
		sentinel = curr = ListNode(0)
		p1, p2 = list1, list2
		while p1 and p2:
			if p1.val < p2.val:
				curr.next = p1
				p1 = p1.next
			else:
				curr.next = p2
				p2 = p2.next

			curr = curr.next

		# merge what's left
		curr.next = p1 or p2

		return sentinel.next

	# time: O(N log K), K is the length of lists, N is total number of nodes
	# space: O(1) since we merge two sorted LL in O(1) space

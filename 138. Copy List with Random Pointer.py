from typing import *


# Definition for a Node.
class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random


class Solution:
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		# approach 1: Iteration + hash map (two passes)
		# 1. Create a hash map mapping from the old node in the original list to a new node in the deep-copied list. Inn the first pass by traversing each node in the original list
		# 2. In the orignal list, if the random pointer of node A points to node C. We can link the cloned node A points to the cloned node C by using the hash map since it contains the mapping between node C and cloned node C. This applies to the next pointer of node A also. We continue to do it for each cloned node while traversing each node in the original list
		# step 1
		oldToCopy = {None: None}
		# key is the original node from original list
		# val: is the cloned node of the copied list
		curr = head
		while curr:
			cloned = Node(curr.val)
			oldToCopy[curr] = cloned
			curr = curr.next

		# step 2
		curr = head
		while curr:
			cloned = oldToCopy[curr]
			cloned.next = oldToCopy[curr.next]
			cloned.random = oldToCopy[curr.random]
			curr = curr.next

		return oldToCopy[head]

# time: O(n), space: O(n), n is the length of the LL

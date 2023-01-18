# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		# copy the next node's value to the current node's val
		# update the next next node ref to the curr node's next
		node.val = node.next.val
		node.next = node.next.next  # since the curr node is guranteed not the tail node

	# time: O(1), space: O(1)

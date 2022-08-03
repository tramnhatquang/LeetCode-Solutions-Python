# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		# APPROACH 1: For each node in list A, traverse over list B and check whether or not the node is present in list B.
		#         while headA:
		#             pB = headB
		#             while pB:
		#                 if headA == pB:
		#                     return headA
		#                 pB = pB.next

		#             headA = headA.next

		#         return None

		# Time: O(N * M), Let N be the length of list A and M be the length of list B.
		# space: O(1)

		# APPORACH 2: Using a hash table
		# Traverse list B and store the address/reference of each node in a hash table. Then for each node in list A, check whether or not that node exists in the hash table. If it does, return it as it must be the intersection node. If we get to the end of list A without finding an intersection node, return null.

		# The one thing we need to be careful of is that we're comparing objects of type Node. We don't want to compare the values within the nodes; doing this would cause our code to break when two different nodes have the same value.

		#         nodes_in_B = set()
		#         while headB:
		#             nodes_in_B.add(headB)
		#             headB = headB.next

		#         while headA:
		#             if headA in nodes_in_B:
		#                 return headA
		#             headA = headA.next

		#         return None

		# TIme: O(N + M), N and M are lengths of A and B respectively
		# SPACE: O(M)

		## APPROACH 3: Two Pointers technique
		# 1.Set pointer pA to point at headA.
		# 2. Set pointer pB to point at headB.
		# 3. While pA and pB are not pointing at the same node:
		#   If pA is pointing to a null, set pA to point to headB.
		#   Else, set pA to point at pA.next.
		#   If pB is pointing to a null, set pB to point to headA.
		#   Else, set pB to point at pB.next.
		# 4. Return the value pointed by pA (or by pB, they are the same now)

		pA, pB = headA, headB
		while pA != pB:
			pA = pA.next if pA else headB
			pB = pB.next if pB else headA

		return pA

# time: O(N + M) where N, M are the lengths of A, B respectively
# space: O(1)

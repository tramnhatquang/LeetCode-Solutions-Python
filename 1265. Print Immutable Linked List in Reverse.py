# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
class ImmutableListNode:
	def printValue(self) -> None:  # print the value of this node.
		pass
	def getNext(self) -> 'ImmutableListNode':  # return the next node.
		pass

class Solution:
	def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
		# approach 1: Recursion
		# Time = space = O(n)
		# 1. if the current node is not None, recursively get the next node until reaching the last node in the LL
		# 2. For each recursive call, we call printValue() after the getNext() call. Eventually, we will have a reverse linked list value

		# if head:
		#     self.printLinkedListInReverse(head.getNext())
		#     head.printValue()

		# time = space = O(n)

		# approach 2: Iteration, using stack
		# time = space = O(n)
		# if not head:
		#     return None
		# stack = []
		# while head:
		#     stack.append(head)
		#     head = head.getNext()
		# while stack:
		#     stack.pop().printValue()

		# approach 3: Reduce the space complexity to O(1) but the time complexity is O(n^2)
		#         last_print = None
		#         while last_print != head:

		#             # find the previoous node
		#             curr = head
		#             while curr.getNext() != last_print:
		#                 curr = curr.getNext()
		#             curr.printValue()

		#             last_print = curr

		# approach 4: SQUARE ROOT DECOMPOSITION
		# reduce the length of the LL into smaller chuncks to speed up processing

		def count(head):
			cnt = 0
			while head:
				cnt += 1
				head = head.getNext()
			return cnt

		def getHeadNodes(head, step):
			cnt = 0
			ans = []
			while head:
				if cnt % step == 0:
					ans.append(head)
				head = head.getNext()
				cnt += 1
			return ans

		def printReverse(head, step):
			cnt = 0
			st = []
			while head != None and cnt < step:
				st.append(head)
				head = head.getNext()
				cnt += 1
			while st:
				st.pop().printValue()

		step = int(sqrt(count(head))) + 1
		headNodes = getHeadNodes(head, step)
		while headNodes:
			printReverse(headNodes.pop(), step)

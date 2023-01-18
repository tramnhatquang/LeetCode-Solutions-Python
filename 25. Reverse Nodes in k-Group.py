from typing import *


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
		dummy = ListNode(0, head)
		groupPrev = dummy

		while True:
			kth = self.getKth(groupPrev, k)
			if not kth:
				break
			groupNext = kth.next

			# reverse group
			prev, curr = kth.next, groupPrev.next
			while curr != groupNext:
				tmp = curr.next
				curr.next = prev
				prev = curr
				curr = tmp

			tmp = groupPrev.next
			groupPrev.next = kth
			groupPrev = tmp
		return dummy.next

	def getKth(self, curr, k):
		while curr and k > 0:
			curr = curr.next
			k -= 1
		return curr

	def printLL(self, head: ListNode) -> List[int]:
		res = []
		while head:
			res.append(head.val)
			head = head.next

		return res


if __name__ == '__main__':
	head = ListNode(5)
	head.next = ListNode(10)
	head.next.next = ListNode(20)
	head.next.next.next = ListNode(30)
	head.next.next.next.next = ListNode(40)

	s = Solution()
	head = s.reverseKGroup(head, 2)
	print(s.printLL(head))

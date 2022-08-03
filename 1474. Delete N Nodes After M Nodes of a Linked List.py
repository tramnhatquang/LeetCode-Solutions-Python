# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = prev = head
        while curr:
            m_count = m
            n_count = n
            while curr and m_count != 0:
                prev = curr
                curr = curr.next
                m_count -= 1

            while curr and n_count != 0:
                curr = curr.next
                n_count -= 1
            prev.next = curr

        return head
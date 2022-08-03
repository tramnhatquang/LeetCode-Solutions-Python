# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Time: O(n)
        # Space: O(1)
        # res = head.val
        # while head.next:
        #     res = res * 2 + head.next.val
        #     head = head.next
        # return res

        # Bit Manipulation Method
        # res = 0
        # while head:
        #     res = res << 1 | head.val
        #     head = head.next
        # return res

        # ANother approach:
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next

        return res
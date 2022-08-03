from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute-force solution
        # Time = Space = O(n) where n is the length of the linked list
        # arr = []
        # while head:
        #     arr.append(head)
        #     head = head.next
        # return arr[len(arr) // 2]

        # Second approach is to use a fast and slow pointer
        # Time: O(n) where n is the length of the linked list
        # Space: O(1)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

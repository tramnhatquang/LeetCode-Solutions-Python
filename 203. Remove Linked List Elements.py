from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements_iterative_optimal(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # we use the dummy node to avoid the case when the head is removed because head's val == val
        dummy = ListNode(0, head)
        curr = dummy
        while curr and curr.next:
            # To remove the val from the LL, we have to keep track of the preceding node's reference to update its next node
            # we do not move the pointer until the curr.next.val != val
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
        # time: O(n), n is length of LL
        # space: O(1)

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # recursive approach

        # base case
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

        # time = space = O(n), n is length of LL

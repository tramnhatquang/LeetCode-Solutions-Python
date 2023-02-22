# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currHead = head
        dummy = prev = ListNode(0, head)

        # We will traverse the original list and skip all the duplicates since duplicates are consecutive in sorted order. When we reach a distinct node, connect curr.next = currHead and move the curr to the next pointer.
        # We keep doing that until the currHead is None
        while currHead:
            if currHead.next and currHead.next.val == currHead.val:
                while currHead.next and currHead.next.val == currHead.val:
                    currHead = currHead.next
                # connect the last distinct node to the next distinct node
                prev.next = currHead.next
            else:
                prev = prev.next
            currHead = currHead.next
        return dummy.next

        # time: O(n), n is length of arr
        # spacE: O(1)

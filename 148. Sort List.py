# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. append all values into a list
        # 2. Then, sort the list
        # 3. Build a new LL based on the sorted list
        sorted_list = []
        curr = head
        while curr:
            sorted_list.append(curr.val)
            curr = curr.next
        sorted_list.sort()

        dummy = curr = ListNode()
        for i in range(len(sorted_list)):
            curr.next = ListNode(sorted_list[i])
            curr = curr.next
        return dummy.next

        # time: O(n log n) due to the Timsort
        # space: O(n)

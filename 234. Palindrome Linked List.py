
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome_optimal(self, head: Optional[ListNode]) -> bool:
        # use fast, slow pointer to find the middle ListNode
        # 1. reverse the second half using the middle ListNode
        # 2. Using two pointer, one pointing to the head of LL, one pointing to the head of the reversed LL
        # 3. Compare the values of two pointers, if they are not equal, return False. Otherwise, advance them together to the next pointers
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # now slow points at the middle node
        # then reverse the second half
        end_first_half = slow
        head_second_half = self.reverse(slow.next)
        p1, p2 = head, head_second_half
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        # 1 -> 2 -> 3 ->4
        #      s    f
        # reverse the second half to its original
        end_first_half.next = self.reverse(head_second_half)
        # print(f'\tAfter restoring the list: {head}')
        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def isPalindrome_not_optimal(self, head: Optional[ListNode]) -> bool:
        # append all nodes values into the list
        # check if we have a palindromic list or not
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        left, right = 0, len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True

        # time = space = O(n)

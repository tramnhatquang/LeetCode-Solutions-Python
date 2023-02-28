n# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        - Start adding 1 from the least significant digit. If the value of a node > 10, we take curr.val = sum % 10, and carry = sum // 10
        - Keep adding carry to all the nodes from the end. One edge case is when all nodes values are [9, 9, 9], so after adding the carry, the left carry is 1 and we need to create a new Node(1) as the head
        """
        def reverse(head: ListNode) -> ListNode:
            # reverse the linked list in-place
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev 

        tail = reverse(head)
        curr = tail
        carry = 1
        while carry and curr:
            sum = curr.val + carry
            curr.val = sum % 10
            carry = sum // 10
            curr= curr.next

        # in case we have [9, 9, 9] -> [0, 0, 0, 1] -> we have to take care if curr is None but carry = 1

        head = reverse(tail)
        if carry:
            new_node = ListNode(1, head)
            return new_node
    
        return head
    
    # time: O(n) = space, n is length of LL












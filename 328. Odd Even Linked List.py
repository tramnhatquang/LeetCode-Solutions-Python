# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Algo:
                1. Initialize 3 pointers (odd, evenHead,  even) to help us keep track of all the nodes
                2. For each iteration,
                    - we connection odd.next = odd.next.next
                    - we connection even.next = even.next.next
                    - After that, we update odd = odd.next, even = even.next to continue updating the next nodes
                We keep doing this until even is Null or even.next is Null, since even will be the last pointer helping us when to stop iteration. 

                3. We link odd (pointing at the last node in the odd LL) to the evenHead.
        """
        # check if the head is None or ther is only one node in the LL
        if not head or not head.next:
            return head

        odd = head
        evenHead = even = head.next
        # even is not null and even.next is not null, helping us to know when to stop
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead
        return head

        # time: O(n), spacE: o(1)

    def oddEvenList_not_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            - Append all values into a list
            - Build a new LL using odd and even indices

        """
        dummy = ListNode(0)
        values = []  # stores all values in the LL
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        curr = dummy
        for i in range(0, len(values), 2):  # build all odd indices first (1 indexed based)
            curr.next = ListNode(values[i])
            curr = curr.next

        for i in range(1, len(values), 2):  # build all even indices later
            curr.next = ListNode(values[i])
            curr = curr.next

        print(f'Values: {values}')
        return dummy.next

        # time: O(n) = space

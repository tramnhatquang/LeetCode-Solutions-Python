# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        """
        Process to LLs at the same 
        1. Initialize a dummy node that helps us to keep track of the head of merged LL. Initialize a curr node = dummy node that helps us to keep track of the current node while traversing
        2. If the head of a LL has a larger power, we add the current power and coefficient to the curr node and move the larger head ahead
        3. If two heads have the same power, we add the sum of their coefficients and its power as values to the answer list
        """
        p1, p2 = poly1, poly2
        dummy = curr = PolyNode()
        while p1 and p2:
            if  p1.power < p2.power:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
            elif p1.power > p2.power:
                curr.next =  p1
                p1 = p1.next
                curr = curr.next
            else: # two heads have same power, take the sum of their coefficients
                sum_coefficient = p1.coefficient + p2.coefficient
                if sum_coefficient: # check if coefficient != 0
                    curr.next = PolyNode(sum_coefficient, p1.power)
                    curr = curr.next
                # move both heads
                p1 = p1.next
                p2 = p2.next
        curr.next = p1 or p2
        return dummy.next

        # time: O(n + m), n, m are lengths of both LLs
        # space: O(n + m)







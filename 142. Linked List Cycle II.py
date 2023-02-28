from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The trick is to use slow, fast pointers to solve this problem. The node is located at where slow and fast pointer meet will be the key to solve this problem. If we detect a cycle in the LL, we initialize a curr pointer from the head, and a second pointer pointing to the intersection. We advance them until they meet
        """
        slow = fast = head
        # find the node where slow and fast meets
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # the else statement only be executed when the while loop returns false
            return None
        curr = 64
        while curr != slow:
            curr = curr.next
            slow = slow.next

        return curr

        # time: O(n), n is number of nodes in the LL
        # space: O(1)

    def detectCycle_set(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use a HashSet to keep track of nodes that we've already seen in a Set(), we can traverse thr list and return the first duplicate node
        """
        visited_nodes = set()
        curr = head
        while curr:
            if curr not in visited_nodes:
                visited_nodes.add(curr)
                curr = curr.next
            else:
                # we have a duplicate node and it is start of the cycle
                return curr
        return None

    # time = space =  O(n), n is the number of nodes

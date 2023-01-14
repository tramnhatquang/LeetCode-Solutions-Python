from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthNodeFromTheEnd(head: 'ListNode', n: int) -> 'ListNode':
    dummy = ListNode(0, head)
    slow = fast = dummy
    # move the fast pointer so that the gap between the slow and fast pointer is n nodes apart
    for _ in range(n + 1):
        fast = fast.next
    # move two pointer simultaneously to the end of LL
    while fast:
        fast = fast.next
        slow = slow.next

    # slow ponits at (n+1) th node from the end
    slow.next = slow.next.next
    return dummy.next


def printLL(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def longestPalindrome(s: str) -> str:
    if not s:  # make sure we do not have empty string
        return ''
    n = len(s)
    longest_palindromic_count = 0  # since a character is a palindromic
    longest_palindromic = ''
    for i in range(n):
        # if odd length
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > longest_palindromic_count:
                longest_palindromic = s[left:right + 1]
                longest_palindromic_count = right - left + 1
            left -= 1
            right += 1

        # if even length
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            # while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) > longest_palindromic_count:
                longest_palindromic = s[left:right + 1]
                longest_palindromic_count = right - left + 1
            left -= 1
            right += 1

    return longest_palindromic


def serialize(root: TreeNode) -> str:
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    res = []
    queue = deque([root])
    while queue:
        curr_length = len(queue)
        for _ in range(curr_length):
            node = queue.popleft()
            if not node:
                res.append('null')
            else:
                res.append(node.val)
            # append the left and right subtrees
            queue.append(node.left)
            queue.append(node.right)

    return ','.join(res)


# time: O(n^2), space: O(1)

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.left.right = TreeNode(10)

    #          5
    #        /   \
    #      3      6
    #       \    /  \
    #	   10  7     8

    print(serialize(root))

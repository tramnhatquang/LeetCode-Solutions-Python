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


# time: O(n^2), space: O(1)

if __name__ == '__main__':
	assert longestPalindrome('babad') == 'bab'
	assert longestPalindrome('cbbd') == 'bb'

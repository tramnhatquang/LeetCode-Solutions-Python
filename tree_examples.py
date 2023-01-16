class TreeNode:

	def __init__(self, val=0, left=None, right=None) -> None:
		self.val = val
		self.left = left
		self.right = right


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


def serialize(root):
	if root is None:
		return '#'
	return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))


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

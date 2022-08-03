# build a Node class to rrepresent each node in the LL
class ListNode:
	def __init__(self, val=0):
		self.val = val
		self.next = None


class MyLinkedList:

	def __init__(self):
		self.head = ListNode()
		self.size = 0

	# O(k) for time complexity
	def get(self, index: int) -> int:
		# check if index is invalid
		if index < 0 or index >= self.size:
			return -1

		curr = self.head
		# curr needs to move from the sentinel head
		for i in range(index + 1):
			curr = curr.next

		return curr.val

	# time: O(1)
	def addAtHead(self, val: int) -> None:
		# we can implement addAtIndex and use addAtIndex(0, val) for this function
		self.addAtIndex(0, val)

	# Time: O (N), N is the length of LL
	def addAtTail(self, val: int) -> None:
		self.addAtIndex(self.size, val)

	# time: O(k), k is the index of the element to be added
	def addAtIndex(self, index: int, val: int) -> None:
		# if index is larger than the size, the node will not be isnerted
		if index > self.size:
			return

		# create a new node
		new_node = ListNode(val)

		# find the predessor of the node to be added
		pred = self.head
		for i in range(index):
			pred = pred.next

		# insert the new node
		new_node.next = pred.next
		pred.next = new_node
		self.size += 1

	def deleteAtIndex(self, index: int) -> None:

		# check if we have a valid index, do nothing
		if index < 0 or index >= self.size:
			return

		self.size -= 1

		# find the predessor of the node to be deleted
		pred = self.head
		for _ in range(index):
			pred = pred.next

		# delete the pred.next
		pred.next = pred.next.next

# space complixity for all functions: O(1)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

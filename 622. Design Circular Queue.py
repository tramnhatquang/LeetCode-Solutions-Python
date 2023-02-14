class DoublyLinkedListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:
    """Implemented the Circular Queue using  Doubly Linked List Node
    
    Look far more below for the implementation using array
    """
    def __init__(self, k: int):
        # Use two dummy nodes to help us with insertion, deletion
        # Initially, two dummy nodes link together
        self.space = k
        self.left = DoublyLinkedListNode(0)
        self.right = DoublyLinkedListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # create a new node
        new_node = DoublyLinkedListNode(value, self.right, self.right.prev)
        # append new node to the left side of the right dummy node
        self.right.prev.next = new_node
        self.right.prev = new_node
        self.space -= 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # remove the node from the left dummy node
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

    # time: O(1) for all operations
    # space: O(k)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class MyCircularQueue_1:

    """Implementaion using array 
    """
    def __init__(self, k: int):
        self.arr = [0] * k
        self.left = 0
        self.right = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        # if queue is full -> False
        if self.isFull():
            return False
        # append the new value into the right pointer
        self.arr[self.right] = value
        #update right pointer
        self.right = (self.right + 1) % len(self.arr)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # update the left pointer
        self.left = (self.left + 1) % len(self.arr)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.right - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return len(self.arr) == self.size
    
    # time: O(1) for each operation
    # space: O(k)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
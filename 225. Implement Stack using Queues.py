import collections


class MyStack:
    """
    Using two queues to solve this problem
    - 
    """

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        # push the curr element to the end of the queue
        self.queue.append(x)

    def pop(self) -> int:
        # use a temp queue

        # temp = collections.deque()
        # while self.queue and len(self.queue) != 1:
        #     temp.append(self.queue.popleft())

        # removed_element = self.queue.popleft()
        # self.queue = temp # assign the temp queue back to queue
        # return removed_element
        """Without using a temp queue
            - Append all elements back into the end of the queue except the last element
        """
        for _ in range(len(self.queue) - 1):
            self.push(self.queue.popleft())

        # return the removed element
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

    # time: O(1) for all operations except pop() method. pop() method takes O(n) time complexity
    # space: O(n)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

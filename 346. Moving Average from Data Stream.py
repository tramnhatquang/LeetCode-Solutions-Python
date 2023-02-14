class MovingAverage_1:
    """
    Applying the concept of circular queue. The tail of queue is connected to the head of it. The circular queue's size == size
    """

    def __init__(self, size: int):
        self.queue = [0] * size
        self.size = size
        self.count = 0
        self.head = self.window_sum = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:
    """
    Use a deque (double-ended queue) to solve this problem.  We only need to keep track a window length of size. Whenever, we get over the original size, we pop it out from the current queue and append a new one. Keep track of a running sum
    """

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.count = 0
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)

        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum + val - tail
        return self.window_sum / min(self.count, self.size)

    # time: O(1) for all operations
    # space: O(size) for the queue's size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

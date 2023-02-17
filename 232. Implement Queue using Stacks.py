class MyQueue:

    def __init__(self):
        self.old_stack = []
        self.new_stack = []

    def push(self, x: int) -> None:
        """
        Append new value into the old stack
        """
        self.old_stack.append(x)
    # time: O(1), space: O(n)

    def pop(self) -> int:
        """
        Pop the top value from the new stack
        """
        self.shift_stack()
        return self.new_stack.pop()

    def peek(self) -> int:
        self.shift_stack()
        return self.new_stack[-1]

    def empty(self) -> bool:
        return not self.old_stack and not self.new_stack
    
    def shift_stack(self):
        if not self.new_stack:
            while self.old_stack:
                self.new_stack.append(self.old_stack.pop())

    # time: 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
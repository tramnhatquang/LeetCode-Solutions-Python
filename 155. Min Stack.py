class MinStack:
	# The observation is that we have to store the min value of each node in the stack

	def __init__(self):
		self.size = 0
		self.stack = []  # (key, min_val)

	def push(self, val: int) -> None:
		# check if the stack is empty. If it is, the min value is the first value, else , the min value of each key is the min of the current key including prev keys
		if not self.stack:
			self.stack.append((val, val))
		else:
			self.stack.append((val, min(self.stack[-1][1], val)))

	def pop(self) -> None:
		self.stack.pop()

	def top(self) -> int:
		if self.stack:
			return self.stack[-1][0]
		return -1  # if the stack is empty

	def getMin(self) -> int:
		if self.stack:
			return self.stack[-1][1]
		return -1  # if the stack is empty


class MinStack:

	def __init__(self):
		self.min_stack = []
		self.stack = []

	def push(self, val: int) -> None:
		self.stack.append(val)
		if not self.min_stack or self.min_stack[-1] >= val:
			self.min_stack.append(val)

	def pop(self) -> None:
		if self.min_stack[-1] == self.stack[-1]:
			self.min_stack.pop()
		self.stack.pop()

	# time: O(1)

	def top(self) -> int:
		if self.stack:
			return self.stack[-1]
		return -1  # if the stack is empty

	# time: O(1)
	def getMin(self) -> int:
		if self.min_stack:
			return self.min_stack[-1]
		return -1  # if the min stack is empty

# time: O(1)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

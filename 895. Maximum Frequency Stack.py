import collections


class FreqStack:
	"""
	We can think of custom data structure called stack of stacks
	- We use a stack to keep track of elements with a particular frequency
	Link for more descriptions: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qV9YopEymEG
	"""

	def __init__(self):
		self.frequency = collections.defaultdict(int)
		self.group = collections.defaultdict(list)
		self.max_frequency = 0

	def push(self, val: int) -> None:
		# Get the frequency for the given value
		# and increment the frequency for the given value
		self.frequency[val] += 1
		freq = self.frequency[val]

		# Check if the maximum frequency is lower that the new frequency
		# of the given show
		if freq > self.max_frequency:
			self.max_frequency = freq

		# group all values within same freq
		self.group[freq].append(val)

	def pop(self) -> int:
		if self.max_frequency > 0:
			value = self.group[self.max_frequency].pop()
			# decrement the frequency after popping
			self.frequency[value] -= 1

			if not self.group[self.max_frequency]:
				self.max_frequency -= 1
			return value
		else:
			return -1


# time: O(1) for both pop() and push() method
# space: O(n) where n is the number of elements in FreqStack


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


"""
Native approach:
    - Use a max heap to keep track the max freq number from the FreqStack
    - Need a hash map to store the frequency of each value, and a counter to keep track the most recently inserted element into the stack, which is useful when decicding which element to pop in the case where the frequencies of two or more values are the same
    - The counter is initially set to 0
"""


class FreqStack_1:

	def __init__(self):
		self.freq = collections.defaultdict(int)
		self.max_heap = []
		self.counter = 0

	def push(self, val: int) -> None:
		# increase the frequency of element in the hash map
		self.freq[val] += 1
		heapq.heappush(self.max_heap, (-self.freq[val], -self.counter, val))
		self.counter += 1

	def pop(self) -> int:
		freq, counter, val = heapq.heappop(self.max_heap)
		# decrement the freq of val in hash map
		self.freq[val] -= 1
		# remove completely from the hash map if its freq  =0
		if self.freq[val] == 0:
			del self.freq[val]

		return val

# time: O(log n ) for push() and pop() method
# space: O(n) for the stored values in the hash map

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

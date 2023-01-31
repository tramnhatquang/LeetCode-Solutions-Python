from random import choice


class RandomizedSet:

	def __init__(self):
		self.map = {}
		self.list = []

	def insert(self, val: int) -> bool:
		# return False if val is already in the map
		if val in self.map:
			return False
		self.list.append(val)
		self.map[val] = len(self.list) - 1  # key: number, value: index in the list1
		return True

	# time: O(1) average time complexity

	def remove(self, val: int) -> bool:
		# return False if val is not in the map
		if val not in self.map:
			return False

		# move the value to be deleted to the last element in the list
		# then pop the last element in the list and delete
		last_element, index = self.list[-1], self.map[val]
		self.list[index] = last_element
		self.map[last_element] = index
		self.list.pop()
		del self.map[val]

		return True

	# time: O(1) average time complexity

	def getRandom(self) -> int:
		return choice(self.list)

# time: O(1) average time complexity
# space: O(n)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
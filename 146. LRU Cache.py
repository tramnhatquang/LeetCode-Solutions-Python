# class LRUCache:
# approach 1: OrderedDict
# use the OrderedDict where the order of items in the dict show how recently the items were used. The least recently used item is at the beginning while in the end we have the most recently used

# initializing the capacity
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         """
#         we return the value of the key
#         that is queried in O(1) and return -1 if we
#         don't find the key in out dict / cache.
#         And also move the key to the end
#         to show that it was recently used.
#         """
#         if key not in self.cache:
#             return -1
#         else:
#             # move the item to the last of the dict
#             self.cache.move_to_end(key)
#             return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         """
#         first, we add / update the key by conventional methods.
#         And also move the key to the end to show that it was recently used.
#         But here we will also check whether the length of our
#         ordered dictionary has exceeded our capacity,
#         If so we remove the first key (least recently used)
#         """
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last = False)

# time: O(1) for get() and put() since all operations with ordered dictionary get/in/set/move_to_end/pop_item are done in a constant time
# space: O(capacity) since the cache contains at most capacity elements


# approach 2: Self-implementation of the LRU cache using hash map + doubly linked list

# implementation of the Doubly Linked List Node
class Node:
	def __init__(self, key: int, val: int):
		self.val = val
		self.key = key

		# initialize the next and previous pointer
		self.prev = self.next = None


class LRUCache:
	# Imagine the LRUCache is like a Doubly Linked List where the LRU items are in the beginning while the MRU (most recently used) items are at the back

	# initializing the capacity, the left most and right most
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.cache = {}  # hash map maps the key to its node

		# intialize the left and right most node
		self.left, self.right = Node(0, 0), Node(0, 0)
		self.left.next = self.right
		self.right.prev = self.left

	def insert(self, node):
		"""
        Insert a node to the back of the Doubly Linked List
        """
		prev, nxt = self.right.prev, self.right
		prev.next = nxt.prev = node
		node.next, node.prev = self.right, prev

	def remove(self, node):
		"""
        Remove an existing node from the Doubly Linked List
        """
		prev, nxt = node.prev, node.next
		prev.next = nxt
		nxt.prev = prev

	def get(self, key: int) -> int:
		if key in self.cache:
			# remove the node first
			self.remove(self.cache[key])
			# move the node to the back of the LL
			self.insert(self.cache[key])
			return self.cache[key].val
		return -1  # if not found

	def put(self, key: int, val: int) -> None:
		# remove the node associated with the key from the doubly linked list
		if key in self.cache:
			self.remove(self.cache[key])

		# update the value of key
		self.cache[key] = Node(key, val)

		# insert the node to the back of the LL
		self.insert(self.cache[key])

		if len(self.cache) > self.capacity:
			# remove the LRU item from the beginning of the LL
			lru = self.left.next
			self.remove(lru)
			del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class TimeMap:

	def __init__(self):
		self.map = collections.defaultdict(list)

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.map[key].append([timestamp, value])

	def get(self, key: str, timestamp: int) -> str:
		left, right = 0, len(self.map[key]) - 1
		res = ""

		while left <= right:
			mid = (left + right) // 2
			if self.map[key][mid][0] <= timestamp:
				res = self.map[key][mid][1]
				left = mid + 1
			else:
				right = mid - 1

		return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMap_1:

	# NOTICE: This approach is not efficient

	def __init__(self):
		self.map = collections.defaultdict(dict)

	# example: store as format {'key1': { 1: 'a', 2: 'b'}, 'key2': {}}

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.map[key][timestamp] = value

	# time: O(M * L), M is number of set function calls, L is average length of key and value strings
	# space: O(M*L)

	def get(self, key: str, timestamp: int) -> str:
		if key not in self.map:
			return ""

		print(self.map)
		# iterate on time from 'timestamp' to 1
		for curr_time in range(timestamp, 0, -1):
			print('timestamp: ', timestamp)
			if curr_time in self.map[key]:
				return self.map[key][curr_time]

		return ""

# time: O (N * timestamp * L)
# space: O(1)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

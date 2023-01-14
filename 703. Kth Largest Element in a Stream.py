class KthLargest:
	def __init__(self, k: int, nums: List[int]):
		self.k = k
		self.heap = nums
		heapq.heapify(self.heap)

		while len(self.heap) > k:
			heapq.heappop(self.heap)

	def add(self, val: int) -> int:
		heapq.heappush(self.heap, val)
		if len(self.heap) > self.k:
			heapq.heappop(self.heap)
		return self.heap[0]

# time: O(n * log(n) + m * log(k)), n: length of nums, m is number of calls to add()
# space: O(n)

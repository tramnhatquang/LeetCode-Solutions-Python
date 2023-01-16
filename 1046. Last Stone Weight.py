class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		maxHeap = []

		for n in stones:
			maxHeap.append(-n)
		heapq.heapify(maxHeap)

		while len(maxHeap) > 1:
			stoneA, stoneB = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
			stoneA -= stoneB
			if stoneA:
				heapq.heappush(maxHeap, stoneA)
		if maxHeap:
			return -maxHeap[0]
		else:
			return 0

# time: O(n log n)
# space: O(n)

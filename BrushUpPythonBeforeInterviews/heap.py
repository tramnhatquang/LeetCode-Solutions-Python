# import from the heapq Python library
import heapq

# under the hoods are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 12)

# Min is always at index 0
print(minHeap[0])

# loop over each element in heap
while minHeap:
	print(heapq.heappop(minHeap))

# no max heap by default, work around is to use min heap and multiply by -1
# push and pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -12)
heapq.heappush(maxHeap, -37)

# max is always at index 0
print(-maxHeap[0])

# loop over the maxHeap
while maxHeap:
	print(-heapq.heappop(maxHeap))

# build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
	print(heapq.heappop(arr))

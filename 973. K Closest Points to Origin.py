class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		# use a max heap whose length = k to store k closest distance in the arr

		# the distance between a point and an origin = sqrt(x^2 + y^2)
		heap = []

		for index, point in enumerate(points):
			# store both the distance and the index in the min heap
			x, y = point[0], point[1]
			distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
			print(distance)
			if len(heap) < k:
				heapq.heappush(heap, (-distance, index))
			else:
				if distance > heap[0][0]:
					heapq.heappushpop(heap, (-distance, index))

		print(heap)
		# append all the points corresponding to the indices in the heap
		res = []
		for distance, index in heap:
			res.append(points[index])

		return res

	# time: O(N log k)
	# space: O(k)

import heapq


class Solution:
	def kClosest_better(self, points: List[List[int]], k: int) -> List[List[int]]:
		# use a max heap whose length  =k

		# processing the first k elements:

		n = len(points)
		heap = []

		def distance(point):
			return -(point[0] ** 2 + point[1] ** 2)

		for i in range(k):
			point = points[i]
			heapq.heappush(heap, (distance(point), point))

		# starting processing from k to the last point the arr
		# if the next point > first point in the heap, remove the first point and append the curr point to the heap
		for i in range(k, n):
			point = points[i]
			if distance(point) > heap[0][0]:
				heapq.heappushpop(heap, (distance(point), point))

		res = []
		for _ in range(k):
			dist, point = heapq.heappop(heap)
			res.append(point)
		return res

	def kClosest_not_good(self, points: List[List[int]], k: int) -> List[List[int]]:
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

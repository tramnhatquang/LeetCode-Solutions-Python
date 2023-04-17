class Solution:
	def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
		'''
		-Initial thought: add all students into the class whose average ratio is lowest. However, this seems like a reasonable aprroach but not the optimal one.
		- Basically, we want to add a new student into a class whose potential gain is maximal
		'''

		def findGain(passed, total):
			'''
			find the gain if we add one extra passed student into the class
			'''
			return (passed + 1) / (total + 1) - passed / total

		# find the potential gain for each class and add them into a max heap based on potential gain
		max_heap = []
		for passed, total in classes:
			heappush(max_heap, (-findGain(passed, total), passed, total))

		for i in range(extraStudents):
			_, passed, total = heappop(max_heap)
			# calculate a new gain and append it back to the max heap
			heappush(max_heap, (-findGain(passed + 1, total + 1), passed + 1, total + 1))

		return sum(passed / total for gain, passed, total in max_heap) / len(max_heap)

		# time: O((n + k) log n), n is the number of classes, k is number of student
		# space: O(n)

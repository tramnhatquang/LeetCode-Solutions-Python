import heapq
from collections import Counter


class Solution:
	def reorganizeString(self, s: str) -> str:
		counter = Counter(s)
		max_heap = []
		for char, freq in counter.items():
			# push into a max heap
			heapq.heappush(max_heap, (-freq, char))

		res = []
		previous = None

		# continue the loop until the heap is empty
		while max_heap or previous:
			if previous and len(max_heap) == 0:
				return ""  # no possible string to organize
			# handle the edge case like "aaab"

			count, char = heapq.heappop(max_heap)
			res.append(char)  # add to the result
			count += 1  # since we use max heap, the count is negative, so to decrement it we have to add 1

			# we only add previous back to the heap in the next iteration
			if previous:
				heapq.heappush(max_heap, previous)
				previous = None

			if count:  # update the count
				previous = (count, char)

		return "".join(res)

# time: O(n log c), n is length of string, c is the number of distinct characters in heap
# space: O(log c)

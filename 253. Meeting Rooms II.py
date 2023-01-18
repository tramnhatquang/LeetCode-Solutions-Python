import heapq
from typing import List


class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		# use a heap to solve this question
		# we keep all the rooms in a  min heap where the key for the min heap would be the ending time of meeting

		# algo:
		# 1. Sort the givenn meeting by their start time
		# 2.  Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
		# 3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
		# 4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
		# 5. If not, then we allocate a new room and add it to the heap.
		# 6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

		if not intervals:
			return 0

		# sort it first based on the start time
		intervals.sort(key=lambda x: x[0])

		heap = []

		# add the first meeting's end time since we have to assign it a new room
		heapq.heappush(heap, intervals[0][1])

		for interval in intervals[1:]:
			# if the room due to free up the earliest is free, assign that room to this meeting
			if heap[0] <= interval[0]:
				heapq.heappop(heap)

			# If a new room is to be assigned, then also we add to the heap,
			# If an old room is allocated, then also we have to add to the heap with updated end time.
			heapq.heappush(heap, interval[1])

		return len(heap)

		# time: O(n log n)
		# space: O(n)

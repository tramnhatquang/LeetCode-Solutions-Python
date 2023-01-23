class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		# Sort the intervals based on the starting time
		intervals.sort(key=lambda x: x[0])
		n = len(intervals)

		# make sure that we do not have overlapping consecutive intervals
		for i in range(n - 1):
			start, end = intervals[i][0], intervals[i][1]
			if end > intervals[i + 1][0]:
				return False

		return True
		# time: O(n log n)
		# space: O(n)

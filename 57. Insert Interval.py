class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		i = 0
		n = len(intervals)

		res = []

		# added all intervals that end before the start of the newInterval
		while i < n and intervals[i][1] < newInterval[0]:
			res.append(intervals[i])
			i += 1

		# merge all overlapping intervals to one considering newInterval
		while i < n and intervals[i][0] <= newInterval[1]:
			# update the start time of newInterval
			newInterval[0] = min(newInterval[0], intervals[i][0])
			# update the end time of newInterval
			newInterval[1] = max(newInterval[1], intervals[i][1])
			i += 1

		# add the newInterval into our arr
		res.append(newInterval)

		# add the rest intervals into our res
		while i < n:
			res.append(intervals[i])
			i += 1

		return res

# time: O(n), space: O(1)

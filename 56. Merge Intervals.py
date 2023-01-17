class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:

		# sort them based on the start time

		# use a stack to solve the next part
		# 1. append the first interval into the stack
		# 2. For the next interval, we check if it overlaps with preceding interval. If it does, we merge them and push onto the stack. Otherwise, we keep it the same and push it onto the stack
		# 3. keep doing that until we reach the last of the arr
		# Note: We only need to check the overlapping between the curr and previous interval, not necessarily checking previous previous one since they are all sorted in ascending order

		intervals.sort(key=lambda x: x[0])
		stack = [intervals[0]]
		for interval in intervals[1:]:
			# check if they are overlapping
			start, end = interval[0], interval[1]
			if stack[-1][1] < start:
				stack.append(interval)
			else:
				# merge them to the top interval of the stack
				# only need to update the new end time
				stack[-1][1] = max(stack[-1][1], end)

		return stack

	# time: O(n log n)
	# space: O(n)

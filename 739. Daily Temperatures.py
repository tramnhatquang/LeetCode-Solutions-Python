from typing import *


class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		# approach 1: Monotonic Stack, one pass, left to right
		# alogirithm
		#   1. Initialize a result array that has the same length of temperatures and use default values of all zeroes which help you later when some days do not have warmer temperatures in the future
		#   2. Loop over the array, then store the (val, index) of thhe current day into the stack if the current's temp is not warmer than the temp on the top of the stack. Also, keep checking if the current day's temp is warmer than the temp on the top of the stack, the number of days is the diff between the curr index and the index on the top of the stack and then we populate that diff into the result arr. We should pop  from the stack until the top of the stack is no longer colder than curr temp. When it is done, we can push the curr day onto the stack

		# n = len(temperatures)
		# res = [0] * n
		# stack = [] #(temp, index)
		# for index, temp in enumerate(temperatures):
		#       # Pop until the current day's temperature is not
		#     # warmer than the temperature at the top of the stack
		#     while stack and stack[-1][0] < temp:
		#         prev_temp, prev_index = stack.pop()
		#         res[prev_index] = index - prev_index
		#     stack.append((temp, index))
		# return res

		# time: O(n) = space, n is the length of the input

		# approach 2: Stack, optimized space -Initialize an array answer with
		# the same length as temperatures and all values initially set to 0.
		# Also, initialize an integer hottest = 0 to track the hottest
		# temperature seen so far.

		# - Iterate backwards through the input. At each index currDay,
		# check if the current day is the hottest one seen so far. If it is,
		# update hottest and move on. Otherwise, do the following:

		# - Initialize a variable days = 1 because the next warmer day must be
		# at least one day in the future. - While temperatures[currDay + days]
		# <= temperatures[currDay]: - Add answer[currDay + days] to days. This
		# effectively jumps directly to the next warmer day. - Set answer[
		# currDay] = days. - Return answer.
		n = len(temperatures)
		res = [0] * n
		hottest = 0
		for curr_day in range(n - 1, -1, -1):
			curr_temp = temperatures[curr_day]
			if curr_temp >= hottest:
				hottest = curr_temp
				continue

			days = 1
			while temperatures[curr_day + days] <= curr_temp:
				days += res[curr_day + days]

			res[curr_day] = days

		return res

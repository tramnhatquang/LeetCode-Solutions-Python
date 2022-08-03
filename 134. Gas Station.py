from typing import *


class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		# approach 1: brute force solution
		# 1. Treat each station as a starting point and then travel the cicurlar route to see if you can reach the starting point. During the trip, if the gas balance is negative, that means the gas amount < travel distance between two any gas stations, we are unable to finish the circular route from that starting index.

		# time: O(n^2), n is the length of gas, space: O(1)
		#         for i in range(len(gas)):
		#             # we are unable to move from the i-th station to the (i+1)-th station if the gas[i] - cost[i] < 0
		#             balance = 0
		#             is_possible = True
		#             for j in range(i, len(gas) + i):
		#                 station_index = j % len(gas)
		#                 balance += gas[i] - cost[i]
		#                 if balance < 0:
		#                     is_possible = False
		#                     break
		#             if is_possible:
		#                 return i
		#         return -1

		# approach 2: One pass
		# If we start at i-th index and are unable to reach the j-th index station, that means every station between i and j are unable to reach j. If the sum of all the gas >= sum of all the cost, there must be a solution
		if sum(gas) < sum(cost):
			return -1

		curr_gas = prev_gas = 0
		start = 0
		for i in range(len(gas)):
			curr_gas += gas[i] - cost[i]
			if curr_gas < 0:
				prev_gas += curr_gas
				curr_gas = 0
				start = i + 1

		return start if curr_gas + prev_gas >= 0 else -1

# time: O(n), space: O(1)

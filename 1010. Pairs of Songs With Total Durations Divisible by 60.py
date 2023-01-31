import math
from typing import List


class Solution:

	def numPairsDivisibleBy60_optimal_sol(self, time: List[int]) -> int:
		# solve it in O(n) time
		# - we knwo that all remainders of modulo 60 is [0, 59]
		# - use a hash map to count the occurrence of each remainder
		# - Observation: for each t in time, how many x satisfy (x + t) % 60

		# this can aslo mean x % 60 = 60 - t % 60 for most cases
		# x % 60 = 0 if t % 60 = 0
		# x % 60 = 60 - t % 60, if t % 60 != 0 (to get to the nearest multiple of 60)
		count = [0] * 60
		res = 0
		for t in time:
			remainder = t % 60
			if remainder == 0:
				res += count[0]
			else:
				res += count[60 - remainder]
			count[remainder] += 1

		return res

	# time: O(n), space: O(1)
	def numPairsDivisibleBy60_brute_force_solution(self, time: List[int]) -> int:
		count = 0
		n = len(time)
		for i in range(n):
			for j in range(i + 1, n):
				if (time[i] + time[j]) % 60 == 0:
					count += 1
		return count


# time: O(n^2)
# space: O(1)
# Not time efficient


if __name__ == '__main__':
	print(-10 % 60)
	print(math.fmod(-60, 60))
	print(divmod(-10, 60))

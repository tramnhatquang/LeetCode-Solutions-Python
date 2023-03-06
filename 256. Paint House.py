class Solution:
	def minCost_bottom_up(self, costs: List[List[int]]) -> int:
		"""
		red, blue, green

		[[17,2,17],[16,16,5],[14,3,19]]

		tc: 3*2^(n - 1)

		Optimize the code futher?
		2 + 5 + 3 = 10

		dp[i] will represent the min cost painting the i-th index house  where i is the current house-index we are currently at
		"""
		# this is the bottom-up approach
		n = len(costs)
		k = 3
		dp = [[0] * k for _ in range(n)]
		dp[0] = costs[0]  # base case
		for house in range(1, n):
			for color in range(3):
				if color == 0:  # red house
					dp[house][0] = costs[house][0] + min(dp[house - 1][1], dp[house - 1][2])
				elif color == 1:  # blue house
					dp[house][1] = costs[house][1] + min(dp[house - 1][0], dp[house - 1][2])
				else:  # green house
					dp[house][2] = costs[house][2] + min(dp[house - 1][0], dp[house - 1][1])
		return min(dp[-1])

	# time: O(n) ,n is length of costs
	# space: O(n) due to the recursive calls,

	def minCost_mutate_input(self, costs: List[List[int]]) -> int:
		"""
		We can save some space by mutating the input but it's not recommended in practice
		"""
		num_houses = len(costs)
		for house in range(1, num_houses):
			costs[house][0] += min(costs[house - 1][1], costs[house - 1][2])
			costs[house][2] += min(costs[house - 1][0], costs[house - 1][1])
			costs[house][1] += min(costs[house - 1][0], costs[house - 1][2])

		return min(costs[-1])

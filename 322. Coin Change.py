from typing import List


class Solution:
	def coinChange_bottom_up(self, coins: List[int], amount: int) -> int:
		# let dp[i] denotes the min number of coin to get the i amount
		# the recurrence relation is dp[i] = min(dp[i - coin] + 1, dp[i])
		# Here are more explanations:
		#   - We count + 1 in (dp[i - count] + 1) to count the current coin we pick, and dp[i - coin representing the min number of coin to reach dp[i - count]

		dp = [float('inf')] * (amount + 1)
		dp[0] = 0  # base case since there is 0 coin to reach 0
		for i in range(1, amount + 1):
			for c in coins:
				if i < c:
					continue  # we do not pick c coin since it causes a larger amount than expected
				# update the dp arr
				dp[i] = min(dp[i - c] + 1, dp[i])
		return dp[amount] if dp[amount] != float('inf') else -1

	# time: O(S^n), s is the amount, n is the number of iteration
	# space: O(S) for the arr size

	def coinChange_top_down(self, coins: List[int], amount: int) -> int:
		"""
		dp(S) denotes the min number of coins needed for make change for amount S using coin
		For all coin denominations in the arr, dp(S) = dp(S - c) + 1 where c is all the possble coins in the arr which is our recurrence relations

		"""
		# solve it using top-down approach with memoization to solve this problem
		# this is our recursion func
		memo = {}

		def dp(amount: int) -> int:
			if amount in memo:
				return memo[amount]
			if amount < 0:
				return -1  # we can't make up a negative amount
			elif amount == 0:
				return 0
			min_cost = float('inf')
			for coin in coins:
				sub_min_cost = dp(amount - coin)
				if sub_min_cost != -1:
					min_cost = min(min_cost, sub_min_cost + 1)

			# update the amount into the memo
			memo[amount] = min_cost if min_cost != float('inf') else -1
			return memo[amount]

		return dp(amount)

# time: O(S*n), S is the amount, n is length
# space: O(amount)

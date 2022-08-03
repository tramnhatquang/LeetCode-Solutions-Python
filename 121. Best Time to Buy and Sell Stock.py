from typing import *


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		# approach 1: Brute foce solution
		#   - Use two loops to compute the profit of every possible pair. Use a global variable to keep track of the max profit so far
		# max_profit = 0
		# for start in range(len(prices)):
		#     for end in range(start + 1, len(prices)):
		#         max_profit = max(max_profit, prices[end] - prices[start])
		# return max_profit

		# time: O(n^2), space: O(1), n is the length of the input
		# GIVE TLE

		# approach 2: One pass - Buy low and sell high. We use a variable to
		# keep track of the curr low price so far, and when we are on the day
		# when the price is higher than the min price, we find the profit so
		# far and store it in the max profit
		max_profit = 0
		min_price = float('inf')
		for price in prices:
			if price <= min_price:
				min_price = price
			elif price - min_price > max_profit:
				max_profit = price - min_price

		return max_profit

# time: O(n), n is the length of input
# space: O(1)

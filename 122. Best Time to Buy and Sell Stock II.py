class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		"""
		Instead of keeping track of the minimum price and checking if the current price is greater than the minimum price, we can simply check if the current price is greater than the previous price. If it is, we can add the difference between the current price and the previous price to the maximum profit. Because we know that we can buy on the previous day and sell on the current day (buy low, sell high) to gain profits
		- TC: O(n), n is length of arr
		- Sc: O(1)
		"""

		max_profit = 0
		for i in range(len(prices) - 1):
			if prices[i + 1] > prices[i]:
				max_profit += prices[i + 1] - prices[i]

		return max_profit

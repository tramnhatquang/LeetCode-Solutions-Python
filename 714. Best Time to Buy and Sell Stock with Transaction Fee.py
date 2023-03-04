class Solution:
	def maxProfit(self, prices: List[int], fee: int) -> int:
		n = len(prices)

		if n < 2:  # sanity check
			return 0

		# find the minimum price so far
		min_price = prices[0]
		max_profit = 0
		for price in prices:
			if price < min_price:
				min_price = price
			# we can gain the profit by selling on this day with the transaction fee
			elif price > min_price + fee:
				max_profit += price - min_price - fee
				min_price = price - fee
			# we cannot engage in multiple transactions
			print(f'Min price: {min_price}')
		return max_profit
# time: O(n), n is length of arr
# space: O(1)

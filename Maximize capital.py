from heapq import *


def maximum_capital(c, k, capitals, profits):
	# replace the dummy return with your code
	current_capital = c
	capitals_min_heap = []
	profits_max_heap = []
	# push all the capitals into a min heap
	for index, capital in enumerate(capitals):
		heappush(capitals_min_heap, (capital, index))

	for _ in range(k):
		while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
			c, i = heappop(capitals_min_heap)
			heappush(profits_max_heap, (-profits[i], i))

		if not profits_max_heap:
			break

		j = -heappop(profits_max_heap)[0]
		current_capital += j
	return current_capital

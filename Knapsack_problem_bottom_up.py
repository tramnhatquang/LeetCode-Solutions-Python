def find_knapsack(capacity, weights, values, n):
	# create a table to hold intermediate values
	dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

	for i in range(len(dp)):
		for j in range(len(dp[0])):
			# initialize the table with 0 when either the row or column is 0
			if i == 0 or j == 0:
				dp[i][j] = 0
			# check if the weight of an item is less than the capacity
			elif weights[i - 1] <= j:
				dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]],
				               dp[i - 1][j]
				               )
			# we don't include the item if the weight is greater than the capacity.
			else:
				dp[i][j] = dp[i - 1][j]

	return dp[-1][-1]  # [n][capacity]


# Driver code
def main():
	weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
	values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
	capacity = [6, 3, 3, 10, 20]
	n = [4, 1, 1, 5, 10]

	# Let's uncomment this to see the benefit of using dynamic programming with tabulation

	weights.append([63, 55, 47, 83, 61, 82, 6, 34, 9, 38, 6, 69, 17,
	                50, 7, 100, 101, 4, 41, 28, 119, 78, 98, 38, 75, 35,
	                8, 10, 16, 93, 34, 23, 51, 79, 118, 86, 85, 109, 88,
	                72, 99, 36, 21, 80, 42, 44, 62, 7, 54, 7, 6, 0,
	                65, 25, 44, 86, 76, 18, 11, 10, 104, 17, 36, 91, 78,
	                88, 79, 103, 1, 4, 34, 94, 73, 21, 8, 9, 79, 25,
	                106, 76, 39, 78, 1, 92, 104, 84, 40, 100, 116, 84, 23,
	                79, 109, 79, 71, 72, 116, 90, 79, 26])
	values.append([35, 47, 8, 103, 83, 71, 11, 107, 9, 34, 41, 54, 73,
	               72, 108, 100, 46, 27, 79, 98, 49, 63, 41, 116, 57, 86,
	               51, 47, 88, 118, 65, 0, 64, 11, 45, 47, 36, 50, 114,
	               90, 105, 55, 93, 12, 73, 96, 50, 27, 36, 97, 12, 21,
	               107, 34, 106, 37, 84, 38, 110, 60, 34, 104, 92, 56, 94,
	               109, 81, 17, 24, 106, 50, 68, 90, 73, 46, 99, 5, 5,
	               22, 27, 58, 24, 20, 80, 37, 1, 16, 39, 26, 32, 12,
	               47, 22, 28, 50, 95, 6, 105, 101, 20])
	capacity.append(1000)
	n.append(100)

	for i in range(len(values)):
		print(i + 1, ". We have a knapsack of capacity ", capacity[i],
		      " and we are given the following list of item values and weights:", sep="")
		print("-" * 30, sep="")
		print("{:<10}{:<5}{:<5}".format("Weights", "|", "Values"))
		print("-" * 30)
		for j in range(len(values[i])):
			print("{:<10}{:<5}{:<5}".format(weights[i][j], "|", values[i][j]))
		result = find_knapsack(capacity[i], weights[i], values[i], n[i])
		print("\nThe maximum we can earn is: ", result, sep="")
		print("-" * 100, "\n", sep="")


if __name__ == '__main__':
	main()

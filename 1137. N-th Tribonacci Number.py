class Solution:
	def tribonacci_optimal_space(self, n: int) -> int:
		if n == 0:
			return 0
		elif n == 1 or n == 2:
			return 1

		# using only three variables
		first, second, third = 0, 1, 1
		for i in range(3, n + 1):
			first, second, third = second, third, first + second + third
		return third


# time: O(n), n is the given number
# space: O(1)


def tribonacci_bottom_up(self, n: int) -> int:
	# solve using bottom-up approach with extra arr
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1

	dp = [0] * (n + 1)
	dp[1] = dp[2] = 1
	for i in range(3, n + 1):
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

	return dp[-1]


# time = space = O(n), n is the given number


def tribonacci_top_down(self, n: int) -> int:
	memo = {}

	def dp(i: int) -> int:
		if i == 0:
			return 0
		elif i == 1 or i == 2:
			return 1

		if i in memo:
			return memo[i]

		memo[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)
		return memo[i]

	return dp(n)

# time = space = O(n), n is the given number

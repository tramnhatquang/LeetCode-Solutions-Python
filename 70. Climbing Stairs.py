class Solution:

    def climbStairs_optimal(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3 # reach 2 steps needs 2 ways, reach 3 steps need 3 ways
        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

    def climbStairs_bottom_up(self, n: int) -> int:
        if n <= 2:
            return n

        # an array that represents the answer to the problem for a given state
        dp = [0] * (n + 1)
        dp[1] = 1  # base cases
        dp[2] = 2  # base cases
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # recurrence relation

        return dp[n]

    # time = space =O(n)

    def climbStairs_top_down(self, n: int) -> int:
        # the number of distinct steps climbing to n  = (the number of distinct steps climbing to n - 1) + (the number of distinct steps climbing to n - 2)
        # it's like the fibonaccci sequence where f(n) = f(n - 1) + f(n - 2) where n >= 2, f(0) = 0 , f(1) = 1

        # We can think about using top down recursion with memoization
        def dp(i):
            if i <= 2:
                return i
            if i not in memo:
                # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
                # store the result inside a hashmap to refer to in the future.
                memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]

        memo = {}
        return dp(n)

    # time: O(n) = space

    def climbStairs_brute_force(self, n: int) -> int:
        # use recursion without memoization
        # base case
        if n <= 2:
            return n

        return self.climbStairs_brute_force(n - 1) + self.climbStairs_brute_force(n - 2)
# time: O(2^n)
# space: O(n)

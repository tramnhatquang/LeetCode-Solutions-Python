class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # let dp[i] denotes the min numbe of coints to get the i amount
        # the recurrence relation is dp[i] = min(dp[i - coin] + 1, dp[i])
        # Here are more explainations:
        #   - We count + 1 in (dp[i - count] + 1) to count the current coint we pick, and dp[i - coint] representing the min number of coint to reach dp[i - count]
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # base case since there is 0 coin to reach 0
        for i in range(1, amount + 1):
            for c in coins:
                if i < c:
                    continue  # we do not pick c coin since it causes a larger amount than expected
                # update the dp arr
                dp[i] = min(dp[i-c] + 1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1

    # time: O(S^n), s is the amount, n is the number of iteration
    # space: O(S) for the arr size

from typing import *
from functools import *


class Solution:
    def minCostClimbingStairs_bottom_up_constant_space(self, cost: List[int]) -> int:
        # solve using bottom up aprroach but with only two variables
        down_one = down_two = 0
        for i in range(2, len(cost) + 1):
            # at each iteration, down_one represents the min cost to reach the curr step, down_two will be whatever downOne was prior to the update
            temp = down_one
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp

        return down_one
        # time = O(n), n is length of cost
        # space: O(1)

    def minCostClimbingStairs_bottom_up(self, cost: List[int]) -> int:
        # bottom up Solution
        # the min cost to reach the i-th step is equal to minimumCost[i] = min(minimumCost[i - 1] + cost[i-1], minimumCost[i-2] + cost[i-2])
        # base cases are given as we are allowed to start at either step 0, or step 1, so minimumCost[0] = minimumCost[1] = 0

        # the arr's length shoudl be 1 longer than the length of cost
        # this is because we can treat tyhe "top floor" as a step to reach
        n = len(cost)
        minimum_cost = [0] * (n + 1)
        for i in range(2, n + 1):
            take_on_step = minimum_cost[i-1] + cost[i-1]
            take_two_steps = minimum_cost[i-2] + cost[i-2]
            minimum_cost[i] = min(take_on_step, take_two_steps)

        # the final element in minimum_cost refers to the top floor
        return minimum_cost[-1]

        # time = space =O(n)

    def minCostClimbingStairs_top_down_memoization(self, cost: List[int]) -> int:
        #  top down Solution with memoization
        memo = {}

        def dp(i: int) -> int:
            """Denotes the min cost to reach the i-th step (not including i-th step cost)
            """
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0

            # Check if we have already calculated minimum_cost(i)
            if i in memo:
                return memo[i]
            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + dp(i - 1)
            down_two = cost[i - 2] + dp(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        return dp(len(cost))
        # time = space = O(n)

    def minCostClimbingStairs_python_lru_cache(self, cost: List[int]) -> int:
        #  top down Solution with memoization

        @lru_cache(None)
        def dp(i: int) -> int:
            """Denotes the min cost to reach the i-th step (not including i-th step cost)
            """
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0

            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + dp(i - 1)
            down_two = cost[i - 2] + dp(i - 2)
            return min(down_one, down_two)

        return dp(len(cost))
        # time = space = O(n)

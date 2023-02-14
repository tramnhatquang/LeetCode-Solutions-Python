from functools import *
from typing import *


class Solution:
    
    def findTargetSumWays_top_down(self, nums: List[int], target: int) -> int:
        memo = {} # stores (index, curr_sum) -> number of ways

        def backtrack(index: int, curr_sum: int) -> int:   
            # base case
            # we get to to the last index and totla sum != target
            if index == len(nums):
                return 1 if curr_sum == target else 0
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            memo[(index, curr_sum)] = backtrack(index + 1, curr_sum + nums[index]) + backtrack(index + 1, curr_sum - nums[index])
            return memo[(index, curr_sum)]

        return backtrack(0, 0)

    # time: O(t* n), t is total sum of all numbers, n is length of nums
    # space: O(t *n)
    
    def findTargetSumWays_recursion(self, nums: List[int], target: int) -> int:
        count = 0

        @lru_cache(None)
        def backtrack(index: int, curr_sum: int) -> None:
            nonlocal count
            # base case
            # we get to to the last index and totla sum != target
            if index == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            positive = backtrack(index + 1, curr_sum + nums[index])
            negative = backtrack(index + 1, curr_sum - nums[index])
            return positive + negative

        return backtrack(0, 0)


if __name__ == '__main__':
    s = Solution()
    s.findTargetSumWays([1, 1, 1, 1, 1], 3)

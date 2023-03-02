from functools import *
from typing import *
from typing import Any


class Solution:

    def findTargetSumWays_top_down(self, nums: List[int], target: int) -> int:
	    memo = {}  # stores (index, curr_sum) -> number of ways

	    def backtrack(index: int, curr_sum: int) -> int:
		    # base case
		    # we get to to the last index and totla sum != target
		    if index == len(nums):
			    return 1 if curr_sum == target else 0
		    if (index, curr_sum) in memo:
			    return memo[(index, curr_sum)]
		    memo[(index, curr_sum)] = backtrack(index + 1, curr_sum + nums[index]) + backtrack(index + 1,
		                                                                                       curr_sum - nums[index])
		    return memo[(index, curr_sum)]

        return backtrack(0, 0)

    # time: O(t* n), t is total sum of all numbers, n is length of nums
    # space: O(t *n)

    def findTargetSumWays_recursion(self, nums: List[int], target: int) -> int:

	    @lru_cache(None)
	    def backtrack(index: int, curr_sum: int) -> int | Any:
		    # base case
		    # we get to to the last index and total sum != target
		    if index == len(nums):
			    if curr_sum == target:
				    return 1
			    return 0
		    positive = backtrack(index + 1, curr_sum + nums[index])
		    negative = backtrack(index + 1, curr_sum - nums[index])
		    return positive + negative

	    return backtrack(0, 0)

    def findTargetSumWays_brute_force(self, nums: List[int], target: int) -> int:
	    """
		The brute force solution is to find all expressions using the given numbers and then count the number of expressions that evaluate to the given target. The calculation above shows that we need a recursive solution to make all possible expressions. In other words, we divide the problem into subproblems, and for each number, we place a + or - before it and generate new expressions.
		"""
	    n = len(nums)

	    def helper(start_index: int, curr_sum: int) -> int:
		    # base cases
		    if start_index == n:
			    if curr_sum == target:
				    return 1
			    return 0
		    # for a number, we can either put + sign or - sign in front of it
		    return helper(start_index + 1, curr_sum + nums[start_index]) + helper(start_index + 1,
		                                                                          curr_sum - nums[start_index])

	    return helper(0, 0)
	    # time: O(2^n), n is length of arr
	    # space: O(n) for the recursive calls


if __name__ == '__main__':
	s = Solution()
	s.findTargetSumWays([1, 1, 1, 1, 1], 3)

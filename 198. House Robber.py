class Solution:
    
    def rob_optimal(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    # time: O(n), n is the length of nums
    # spacE: O(1)

    def rob_bottom_up_not_space(self, nums: List[int]) -> int:

        if not nums:
            return 0

        maxRobbed = [None for _ in range(len(nums) + 1)]
        n = len(nums)

        # base case initialization
        maxRobbed[n] = 0
        maxRobbed[n - 1] = nums[n - 1]

        # DP tabulation
        for i in range(n - 2, - 1, -1):
            maxRobbed[i] = max(maxRobbed[i + 1], maxRobbed[i + 2] + nums[i])

        return maxRobbed[0]

        # time = space = O(n)

    def rob_top_down(self, nums: List[int]) -> int:
        memo = {}

        def dp(i: int) -> int:
            # base cases
            if i >= len(nums):  # no more houses to examine
                return 0
            if i in memo:
                return memo[i]

            # get the recurrence relation
            # if we visit the curr house, we haave to skip the next one
            # Otherwise, we can move on to the next house in the list
            ans = max(dp(i + 1), nums[i] + dp(i + 2))
            memo[i] = ans
            return ans

        return dp(0)

        # time = space = O(n), n is the length of nums

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Hint: since the last house is connected to the first house 
            -> IF we start robbing the first house, then we have to skip the last house
            -> If we start robbing the last house, we have to skip the first house
            -We can re-use the DP solution from the House Robber 1 to solve this
            -> Find the DP of robbing from first house to the second last house (1)
            -> Find the DP of robbing from the second house to the last house (2)           
            -> Compare the max betweeen (1), (2) solution
        """
        if len(nums) == 1:
            return nums[0]

        def rob_helper(nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))

        # time = O(n)
        # spacE: O(1)

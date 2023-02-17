class Solution:

    def canJump_optimal(self, nums: List[int]) -> bool:
        """
        The goal is to reach the last index in the arr from the start
            - We can try to iterate from the end to start
            - For each index, we check if the (curr_index + nums[curr_index] >= the current good index, where the curr good index will lead us to the last index in the arr, if it is, then we assign the good_index = curr_index)

        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return True if goal == 0 else False
        # time: O(n)
        # space: O(1)

    def canJump(self, nums: List[int]) -> bool:
        canReach = 0

        for i in range(len(nums)):
            if i <= canReach:
                canReach = max(canReach, i + nums[i])

        return canReach >= len(nums) - 1

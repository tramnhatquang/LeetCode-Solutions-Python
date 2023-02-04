import random


class Solution:

    def rearrangeArray_optimal(self, nums: List[int]) -> List[int]:

        # First, we sort the arr then put it in a pattern like this
        # [nums[0], nums[n - 1], nums[1], nums[n-2], ... nums[k]]
        # The trick here is to make sure the neighbors of a large middle number are smaller than itt. Similarly, the neighbors of a smaller middle number are larger than the middle
        # The pattern like this: small big small big small
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n // 2):
            res.append(nums[i])
            res.append(nums[n-i-1])
        if n % 2:  # if lenght of arr is odd
            res.append(nums[n // 2])
        return res

        # time: O(n log n), space: O(n) due to sorting
    def rearrangeArray_never_try(self, nums: List[int]) -> List[int]:
        """
        Shuffle the arr until it satisfies the condition
        """
        # this approach is chilling. Never try this in an interview
        def isSatisfied(nums) -> bool:
            for i in range(1, len(nums) - 1):
                if nums[i] * 2 == nums[i - 1] + nums[i + 1]:
                    return False
            return True

        while True:
            random.shuffle(nums)
            if isSatisfied(nums):
                return nums
        # time: I do not know the TC and space complexity

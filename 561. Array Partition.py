class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        The key observation here is that if we have a pair like (a,b)(a, b)(a,b) such that a≤b  ba≤b, then we will add aaa to the answer and bbb cannot be used anymore. Therefore, in each such pair, we will add the value of the smaller element but the greater element will not contribute to the answer.
        
        We want to pair the smallest number with the next smallest number to maximize the sum of min pairs
        """
        nums.sort()
        n = len(nums)
        total = 0
        for i in range(0, n, 2):
            total += nums[i] # since we add the min(nums[i], nums[i +1]) = nums[i] since the list is sorted
        
        return total

        # time: O(n log n) due to sorting
        # spacE: O(n)


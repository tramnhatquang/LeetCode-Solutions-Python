class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Brute force solution: Try all possible triplets and see if they satisfy the condition where (i, j, k) such that i < j< k and nums[i] < nums[j] < nums[k]
        TC: O(n^3) -> Not efficient

        This is a special case of LIS.
        LIS can be solved with O(N log M) where M is the length of sequences (generally M is N).
        In this question, we can set M as 3 thus the problem can be solved with O(N) with the general LIS approach.

        The idea is baed on finding the LIS (Longest Increasing Sequence in Leetcode number 300). 
            - Find the first and second number that are in the increasing order then Find the third number which is bigger than both first and second number
        """
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else: # the curr num is larger than first, second num
            # which is third number in the triplet we're looking for
                return True
        return False

        # time: O(n), space: O(1)
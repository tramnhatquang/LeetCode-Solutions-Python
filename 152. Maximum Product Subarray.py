class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Use Dynamic Programming to solve this problem

        Have to not only keep track of the max product so far, but also need to keep track of min product so far
        """
        res = max(nums)
        cur_min, cur_max = 1, 1
        for n in nums:
            tmp = cur_max
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(n * tmp, n * cur_min, n)
            res = max(res, cur_max)
        return res
        # time = O(n), space: O(1)

    def maxProduct_brute_force(self, nums: List[int]) -> int:
        """
        Find products of all subarrays and record te max product so far
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        max_product = nums[0]
        for i in range(n):
            curr_product = 1
            for j in range(i, n):
                curr_product *= nums[j]
                max_product = max(max_product, curr_product)

        return max_product
        # time: O(n^2)
        # space: O(1)

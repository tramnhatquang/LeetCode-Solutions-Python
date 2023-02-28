class Solution:

    def numSubarrayProductLessThanK_optimal(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        # use the sliding window technique
        left = ans = 0
        curr_product = 1

        for right in range(len(nums)):
            curr_product *= nums[right]
            while curr_product >= k:
                curr_product //= nums[left]
                left += 1

            # the trick part is that the newly created arr for each index is equal to right - left + 1 which is window length
            ans += right - left + 1

        return ans
        # time: O(n), space: O(1), n is the length of nums

    def numSubarrayProductLessThanK_brute_force(self, nums: List[int], k: int) -> int:
        """
        The brute force solution is to find all subarrays whose product is strictly less than k 
        """
        if k <= 1:
            return 0
        n = len(nums)
        count = 0
        for i in range(n):
            curr_product = 1
            for j in range(i, n):
                curr_product *= nums[j]
                if curr_product < k:
                    count += 1
        return count

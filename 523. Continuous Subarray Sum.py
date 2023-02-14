class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        The observation is that if two running sum return a same remainder that means there exists a good subrray whose sum % k == 0
        For example, another short version of an explanation: say the the difference is d between a and b, such as d = b - a(b is on the right of a). you want d is multiple of k, so you just need d % k = 0. Because d = b - a, so d % k = 0 = (b - a) %k. so (b-a)%k=0 equal b%k - a%k = 0, then b%k = a%k.

        Algo:
            1. Traverse thr the nums and find the running sum at each index
            2. Check if we hvae the (prefix sum % k) in the map, if not, then store (prefix sum % k) as key and its index as value. Otherwise, we check if the we have at least two elements in the subarray by index.
        If a % k = c, let d is a multiple of k, then d % k == 0 -> (a + d) % k = (a % k) + (d % k) = c + 0 = c
        """
        map_remainder_index = {0: -1}  # incase prefix_sum == k
        prefix_sum = 0
        for index, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            # check in the map
            if remainder not in map_remainder_index:
                map_remainder_index[remainder] = index
            # remainder is in the map, check if we have at least two elements
            elif index - map_remainder_index[remainder] > 1:
                return True
        return False

        # time = O(n)
        # space: O(n)

    def checkSubarraySum_brute_force(self, nums: List[int], k: int) -> bool:
        """
        Brute force solution: Try all possible subarrays and find if their sum is a good subarray or not

        """
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total % k == 0:
                    return True
        return False
        # time: O(n^2), n is length of nums
        # space: O(1)

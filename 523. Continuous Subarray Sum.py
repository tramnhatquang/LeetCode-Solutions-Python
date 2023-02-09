class Solution:

    def maxSubArrayLen_optimal(self, nums: List[int], k: int) -> int:
        """
        Cannot use sliding window to solve this problem since the arr can have negative numbers. We cannot when to expanding/shrinking the window length

        Thinking about using prefix sum + hash map
         - Hash Map stores the key as prefix sum up to the current index (inclusive) and its index as a value. If we have a duplicate prefix sum, we will not update the ahsh map since we want longest subarray, so we want to keep the index as far as possible. 
         - Consider the case when prefix_sum == k, we can explicitly check that or we can initialize our hash map with a key of 0 corrresponding to a value of -1.
        """
        prefix_sum = max_len = 0
        prefix_index_map = {0: -1}
        for index, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                max_len = index + 1
            if prefix_sum - k in prefix_index_map:
                max_len = max(max_len, index -
                              prefix_index_map[prefix_sum - k])

            # only add the current prefix sum index pair to the map
            # if the prefix sum is not already in the map
            if prefix_sum not in prefix_index_map:
                prefix_index_map[prefix_sum] = index

        return max_len

        # time: O(n)
        # space: O(n)

    def maxSubArrayLen_brute_force(self, nums: List[int], k: int) -> int:
        """
        Brute force solution: Try all possible subarrays. In those subarrays whose sum == k, record the max length  
        """
        max_length = 0
        n = len(nums)
        for i in range(n):
            total = 0
            for end in range(i, n):
                start = i
                total += nums[end]
                if total == k:
                    max_length = max(max_length, end - start + 1)
        return max_length

        # time: O(n^2), n is lenght of arr -> NOT TIME EFFICIENT
        # space: O(1)

class Solution:
    def minSubArrayLen_optimal(self, target: int, nums: List[int]) -> int:
        """
        Using a sliding window to solve this problem
        1. Initialize left = 0, n = len(nums), min_length_count = float('inf'), prefix_sum = 0
        2. Traverse thr each number in the nums (right pointer goes from 0 to last index):
          - Add the nums[right] into the prefix_sum
          - while prefix_sum >= target:
            + Record the min_length_count
            + Shrinking the window length to find the min length by increasing left pointer by 1 to the right, and subtract nums[left] from prefix_sum
        3. Return the min_length_count if min_length_count != float('inf') else 0
        """
        left = 0
        n = len(nums)
        min_length_count = float('inf')
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length_count = min(min_length_count, right - left + 1)
                # Shrinking the window length
                curr_sum -= nums[left]
                left += 1

        return min_length_count if min_length_count != float('inf') else 0

        # time: O(n), space: O(1), n is length of arr

    def minSubArrayLen_NOT_OPTIMAL(self, target: int, nums: List[int]) -> int:
        """
        Brute force solution: Find all possible subarrays whose sum >= k and record the min length of those satisfying subarrays
        """
        n = len(nums)
        min_length_count = float('inf')
        for i in range(n):
            total = 0
            for j in range(i, n):
                start = i
                total += nums[j]
                if total >= target:
                    min_length_count = min(min_length_count, j - start + 1)

        return min_length_count if min_length_count != float('inf') else 0
        # time: O(n^2), space: O(1) -> causing TLE

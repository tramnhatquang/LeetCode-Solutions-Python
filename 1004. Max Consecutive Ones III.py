class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        The problem can be understood as find the longest subarray with at most k zeroes

        """
        left = 0
        max_len = 0
        n = len(nums)
        for right in range(n):
            # if we meet a 0, we decrement k by 1
            if nums[right] == 0:
                k -= 1

            # shrink the window whenever k < 0
            if k < 0:
                if nums[left] == 0:
                    k += 1
                # we always move left by 1 no matter when nums[left] = 0 or 1 so that to make sure k >= 0
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
        # time: O(n), space: O(1), n is length of nums

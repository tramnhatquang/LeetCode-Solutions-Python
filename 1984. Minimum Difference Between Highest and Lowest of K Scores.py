class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        # maintain a window of size k and record the min difference of each window
        # min of each window = rightmost  element - leftmost element (since they are sorted)
        # left pointer points at the lowest number in the window
        # right pointer points at the largest number in the window
        left = 0
        right = k - 1
        res = float('inf')
        while right < len(nums):
            res = min(res, nums[right] - nums[left])
            left += 1
            right += 1
        return res

        # time = O(n log n), space: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum, left_sum = sum(nums), 0
        for index, value in enumerate(nums):
            right_sum = total_sum - value - left_sum
            if (left_sum == right_sum):
                return index
            left_sum += value
            
        return -1 # if not found
    # time: O(n), space: O(1)
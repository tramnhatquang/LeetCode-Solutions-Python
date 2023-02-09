class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total
                
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else: # total == target
                    return total
        return closest_sum

        # time: O(n log n)
        # spacE: O(n) due to the timSort









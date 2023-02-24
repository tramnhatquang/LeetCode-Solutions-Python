def find_sum_of_three(nums, target):
    # your code will replace this placeholder return statement
    nums.sort()
    n = len(nums)
    for i in range(n):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                return True
            elif total > target:
                right -= 1
            else:
                left += 1

    return False
    # time: O(n log n)
    # spacE: O(n)

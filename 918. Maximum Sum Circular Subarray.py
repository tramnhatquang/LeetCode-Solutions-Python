class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        The trick here is that we find the max sum subarray that does not wrap around, and max sum subarray that does wrap around. Then find the max of both 

        How do find the max sum subarray that does wrap around?
        To get the largest wrap-around sum, we can use a little trick. For any subarray that wraps around, there must be some contiguous elements that are excluded, and these 
elements actually form the minimum possible subarray! Therefore, we can first find 
the minimum subarray sum using exactly the method above, and subtract this from 
the array's total.
        """

        curr_max = curr_min = 0
        global_max = global_min = nums[0]
        total_sum = 0
        for num in nums:
            curr_max = max(num, curr_max + num)
            curr_min = min(num, curr_max + num)
            total_sum += num  # find the total sum of all elements
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)

        print(f'Global max: {global_max}')
        print(f'Global min: {global_min}')
        # if the minimum so far is the array sum, then all values are negative
        # then just return the answer of Kadane's algorithm: the highest value
        if (global_min == total_sum):
            return global_max

        # returning the maximum value
        return max(global_max, total_sum - global_min)

        # time = O(n), space = O(1)

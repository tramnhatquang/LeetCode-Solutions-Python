class Solution:

    def findPeakElement_optimal(self, nums: List[int]) -> int:
        """
        Using Binary Search to find the peak eleemnt
        1. Initialize left = 0, right = len(nums) - 1
        2. While left <= right:
            - mid = (left + right) // 2
            - if nums[mid] > nums[mid + 1]: we look to the left side since there is a peak and (mid) can be a peak index
            - Otherwise, we look to the right side (from mid + 1 to .. right) to find the peak
        """
        left, right = 0, len(nums) - 1
        boundary_index = -1
        while left <= right:
            mid = (left + right) // 2
            # hande the case when we only have 1 element
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
               # mid couble be a peak
               boundary_index = mid
               right = mid - 1
            else: # nums[mid] < nums[mid + 1] 
                left = mid + 1
        return boundary_index

        # time: O(log n)
        # spacE: O(n)
        
    
    
    def findPeakElement_linear_scan(self, nums: List[int]) -> int:
        """
        Brute force solution: Linear scan
            - For index i in the arr, check if nums[i] > nums[i + 1], then i is a peak in nums
            - There are three possible cases:
                + If we have a descending arr, the first element will be the peak, -> so our solution matches and. In this case, we didn't reach a point where we needed to compare nums[i]nums[i]nums[i] with nums[i−1]nums[i-1]nums[i−1] also, to determine if it is the peak element or not.
                + If we have an ascending arr, the last element will the peak, and we do not need to check if arr[i] > ar[i - 1] since the arr naturally proves that
                + If we have a peak somewhere in the middle at i-th index. We know all the indices before i-th index will be less than i-th index since we are in an ascending order, When we finally reach the peak element, the condition nums[i]>nums[i+1]nums[i] > nums[i + 1]nums[i]>nums[i+1] is satisfied. We again, need not compare nums[i]nums[i]nums[i] with nums[i−1]nums[i-1]nums[i−1].
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i

        return n - 1 # this line is executed only when the arr is ascending
        # time: O(n), space: O(1)


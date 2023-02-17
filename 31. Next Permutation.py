class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Brute force solution:
        1. Find all the permutation of nums and sort it ascending order
        2. The next greater permutation is the next arr that is in the sorted container 
        However, this approach is bad in terms of time efficient since it can take up yo O(n!) time complexity.

        Solution: The problem lies on how to determine the next permutation of the curr array. 
            - The edge case is when we have a decreasing arr like [5, 4, 3, 2] -> next: permutation is [2, 3, 4, 5]

                + In other word, find a[i] and a[i - 1] such that a[i] > a[i- 1]from the right. Now, no rearrangements to the right of a[i−1] can create a larger permutation since that subarray consists of numbers in descending order. 

        """

        n = len(nums)
        if n == 1:
            return
        first_peak_index = n - 1
        # find the first decreasing number from the right such as nums[i - 1] < nums[i] and i goes from right to left
        while first_peak_index > 0 and nums[first_peak_index - 1] >= nums[first_peak_index]:
            first_peak_index -= 1

        # check the edge case when we have a decreasing arr like [9, 8, 7, 6] -> next permutation: [6, 7, 8, 9]
        if first_peak_index == 0:
            nums.reverse()
            return

        first_decrease_index = first_peak_index - 1
        # find the j in the right side of first_decrease_index such that nums[j] > nums[first_decrease_index]
        j = n - 1
        while nums[j] <= nums[first_decrease_index]:
            j -= 1
        # now swap nums[j], nums[first_decrease_index]
        nums[j], nums[first_decrease_index] = nums[first_decrease_index], nums[j]
        # reverse the second part
        left, right = first_decrease_index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # time: O(n)
        # space: O(1)

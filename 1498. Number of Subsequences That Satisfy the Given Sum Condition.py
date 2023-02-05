from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        For each l, move r left until you find the rightmost r that "works" for that l (A[l] + A[r] <= target).

Once you find a valid r for your l, you need to add this number of subsequences to ans.

All of these subsequences will contain l. So you don't need to worry about that. You need to count the number of subsequences in the array from l+1 to r including the empty subsequence! You include the empty subsequence because l on its own is a valid subsequence, so you can combine it with an empty subsequence and still have a valid subsequence.
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right - left, mod)
                left += 1
        return res % mod

        # time: O(n log n)
        # spacE: O(n) due to Timsort

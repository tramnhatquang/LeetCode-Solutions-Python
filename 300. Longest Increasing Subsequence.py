from bisect import bisect


class Solution:
    def lengthOfLIS_optimal(self, nums: List[int]) -> int:
        """The algorithm works as follows:

    1. Initialize an empty list called piles, which represents the piles of cards in the Patience sorting game.
    2. For each number in the input sequence:
        - If the number is larger than the last card in the last pile, add it to a new pile.
        - Otherwise, find the smallest pile whose last card is larger than the number, and replace that card with the number.
    3. The length of the piles list is the length of the longest increasing subsequence.
        """

        # the hardest part of this problem is that we do not if a current number is worth to keep or remove to build a LIS
        # It appears the best way to build an increasing subsequence is: for each element num, if num is greater than the largest element in our subsequence, then add it to the subsequence. Otherwise, perform a linear scan through the subsequence starting from the smallest element and replace the first element that is greater than or equal to num with num. This opens the door for elements that are greater than num but less than the element replaced to be included in the sequence
        piles = []
        for num in nums:
            piles_index = bisect.bisect_left(piles, num)
            if piles_index == len(
                    piles):  # the current number > largest element in our subsequence, add to the subsequence
                piles.append(num)
            else:  # replace the first number in subsequence such that
                piles[piles_index] = num

        return len(piles)

    # time: O(n log n)
    # space: O(n)

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """
        This is the classic DP problem in computer science that asks us to find the longest increasing subsequence (LIS)
        dp[i] represents the length of LIS that ends with the i-th element
        1. Initialize an array of 1 since each element forms an increasing sequence of itself. The array is out base cases
        2. The recurrence relation is that dp[i] = max(dp[j] + 1 for every nums[j] < nums[i] and j < i)
        3. For each element i from 1 to n, compare it to all the previous elements j from 0 to i-1.
        4. If the j-th element is smaller than the ith element and the length of the longest increasing subsequence ending at j is greater than the length of the LIS ending at i, update lis[i] to be lis[j] + 1.
        5. After iterating through all elements i and j, return the maximum element in the lis array.
        """
        n = len(nums)
        res = [1] * n
        for i in range(1, n):  # no need to update the first element since it's the start of LIS
            for j in range(i):
                if nums[j] < nums[i] and res[j] + 1 > res[i]:
                    res[i] = res[j] + 1
        return max(res)

# time: O(n^2), n is the length of nums
# space: O(n)

import collections


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        The optimal way is to store the the cumulative sum as key in the map and its value is the number of occurrences it has happened until the current iteration of the loop as we traverse from left to right
        1. Intialize prefix_sum = 0, sumOccurrencesMap = {0 : 1} (to count for the current subarray if sum of subarray == k), count = 0
        2. When we traverse from left to right, append each number into the prefix_sum, if
            - (prefix_sum - k) in the sumOccurrencesMap, then count += sumOccurrencesMap[prefix_sum - k], counting the number of subarrays whose sum == k
            - After that, always update the sum and its occurrences into the map
            """
        count = 0
        prefix_sum = 0
        sumOccurrMap = collections.defaultdict(int)
        sumOccurrMap[0] = 1  # to count for the firstSubarray whose sum == k
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sumOccurrMap:
                count += sumOccurrMap[prefix_sum - k]
            sumOccurrMap[prefix_sum] += 1

        return count
        # time =  space = O(n)

    def subarraySum_not_optimal(self, nums: List[int], k: int) -> int:
        """
        NOTE: the sliding window will not work here, since if we have negative integers in the arr, the sum of sliding window will decrease as right pointer moves . Ex: [1, 2, -1, 3], res = 3 but sliding window will give 2

 We can choose a particular start point and while iterating over the end points, we can add the element corresponding to the end point to the sum formed till now. Whenever the sus equals the required k value, we can update the count value. We do so while iterating over all the end indices possible for every startindex. Whenever, we update the start index, we need to reset the sum value to 0.
        """
        n = len(nums)
        count = 0
        for left in range(n):
            total = 0
            for right in range(left, n):
                total += nums[right]
                if total == k:
                    count += 1
        return count

        # time: O(n^2), space: O(1)

    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        # brute force solution
        # 1. try all possible subarrays and check if its sum == k then we increase the count
        # 2. Return the count
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                # print(f'Subarray: {nums[i:j + 1]}')
                if sum(nums[i:j + 1]) == k:
                    count += 1

        print(f'Count: {count}')
        return count

        # time: O(n^3), space: O(n)

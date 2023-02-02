from typing import *


class Solution:
    def nextGreaterElement_optimal(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using monotonic decreasing stack to solve this problem
        # we user a hash map and a monotonic stack to solve this problem

        # Algo:
        # 1. Loop over the nums2 arr, and check for each number
        #   - While the stack is not empty and its top number < curr number, then append the curr numebr into the stack.
        #   - Otherwise, we pop the top number from the stack and map[top_number] to its next greater element. In other words, all numbers are popped from the stack whenever we found its next grater element, and the remaining elements in the stack are the ones we have not found its next greater element in the nums2 arr
        # 2. At the end of step 1, we pop from stack and map it to -1 (since we do not find its next greater element)
        res = []
        stack = []
        mapping = {}
        for num in nums2:
            while stack and stack[-1] < num:
                # we found the curr number's next greater
                mapping[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            res.append(mapping.get(num, -1))
        return res

        # time: O(n + m), n, m are lengths of nums2, nums1 respectively
        # space: O(n), to store n numbers in map

    def nextGreaterElement_brute_force(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute force Solution
        # Algo:
        # 1. Initialize a res arr whose length == nums1.length
        # 2. Traverse thr each number in nums1, find its index in nums2
        #   - If its next greater element's index in nums2 is less than nums2.length, assign it back to res[i]
        #   - Otherwise, keep moving on the outer loop
        n, m = len(nums1), len(nums2)
        res = [-1] * n

        for i in range(n):
            number = nums1[i]
            j = nums2.index(number)
            j += 1
            while j < m and nums2[j] < number:
                j += 1
            # now j points at the next greater element of num in nums2
            if j < m:
                res[i] = nums2[j]
        return res

        # time: O(n * (2m)) = O(n*m), where n, m are lengths of nums1, nums2 respectively
        # space: O(n) to store the res arr

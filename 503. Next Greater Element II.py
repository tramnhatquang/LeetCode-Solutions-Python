class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # we still use a monotonic decreasing stack to solve this prob
        # This problem is very similar to Daily Temperatures, except the array is circular. The only change in the implementation is that after the first pass, we do a second pass to find a larger number for the remaining items on the stack without pushing new items in (since they are pushed at least once already in the first pass).
        stack = []  # stores (prev_index, prev_number)
        n = len(nums)
        res = [-1] * n

        for index, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                prev_index, prev_number = stack.pop()
                res[prev_index] = num
            # else, append into the stack
            stack.append((index, num))

        for curr in nums:
            while curr > stack[-1][1]:
                prev_index, prev_num = stack.pop()
                res[prev_index] = curr
        return res
    # time: O(n), space: O(n)

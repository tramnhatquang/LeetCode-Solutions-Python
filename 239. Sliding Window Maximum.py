# import collections
class Solution:

    def maxSlidingWindow_optimal(self, nums: List[int], k: int) -> List[int]:
        # sliding window is a better approach since in the brute force approach, I have done unnecessary, overlapping work
        # Everty time we slide the window, we have to keep track of the max number in the window
        # Larger elements entering the window invalidates smaller elements
# A question we can ask ourselves is "do we need to keep all the window elements in our state?". An important observation is for two elements arr[left] and arr[right], where left < right, arr[left] leaves the window earlier as we slide. If arr[right] is larger than arr[left], then there is no point keeping arr[left] in our state since arr[right] is always gonna be larger during the time arr[left] is in the window. Therefore, arr[left] can never be the maximum.
        # you want to ensure the deque window only has decreasing elements. That way, the leftmost element is always the largest
        res = []
        queue = collections.deque()  # stores indices
        for index, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(index)
            # remove the first element if it's outside the window
            # it likes we maintains only k values in the queue
            if queue[0] == index - k:
                queue.popleft()

            # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if index >= k - 1:
                res.append(nums[queue[0]])

        return res
        # The time complexity is O(N). This is because each element in the original array can only be pushed into and popped out of the deque once.

        # The space complexity is O(N) as there may be at most N elements in the deque.


    def maxSlidingWindow_brute_force(self, nums: List[int], k: int) -> List[int]:
        # brute force Solution
        # traverse thr array and check max value of each subarray whose length == k. And then, we append the max value into the result arr

        # given constraint that 0 <= k <= n, check if either n or k == 0
        n = len(nums)
        if n == 0 or k == 0:
            return []

        res = []
        for i in range(n - k + 1):
            res.append(max(nums[i:i+k]))

        return res
        # timme: O(n * k). It taeks O(n) for the outer loop and O(k) to create a copy of every subarray whose length == k. TC is O(n* k)
        # space: O(k), for the stored res
        # This approach is not efficient

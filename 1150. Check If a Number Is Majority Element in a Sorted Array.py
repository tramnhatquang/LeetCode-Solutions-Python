class Solution:

    def isMajorityElement_no_built_in(self, nums: List[int], target: int) -> bool:

        n = len(nums)
        if nums[n // 2] != target:
            return False

        # if we cannot use the bisect module
        def search_left_most(target: int) -> int:
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    res = mid
                    right = mid - 1
            return res

        left_most_index = search_left_most(target)
        # find the rightmost index if there exists
        possible_index = left_most_index + n // 2
        if possible_index < n and nums[possible_index] == target:
            return True
        return False

        # time: O(log n)
        # space: O(1)

    def isMajorityElement_binary_search(self, nums: List[int], target: int) -> bool:
        """
        Since we are looking at the majority element, if we look at the middle index of the sorted arr and its not equal to target, we do not have a majority element
            - FInd the length of the majority element in the arr
            - If a majority appears in the arr, then we have something like this
                + [x x x _ _]
                + [_ _ x x x]
                + [_ x x x _]

            - We can use the bisect module to find the leftmost, rightmost index to insert the target but still maintain a sorted order

        """
        n = len(nums)
        if nums[n // 2] != target:
            return False

        left_index = bisect.bisect_left(nums, target)
        right_index = bisect.bisect_right(nums, target)

        print(f'left index: {left_index}')
        print(f'Right index: {right_index}')
        return right_index - left_index > n // 2

        # time: O(log n)
        # space: O(1)
    def isMajorityElement_brute_force(self, nums: List[int], target: int) -> bool:
        # brute force solution
        counter = Counter(nums)
        if counter[target] > len(nums) / 2:
            return True
        return False

        # time: O(n) = space

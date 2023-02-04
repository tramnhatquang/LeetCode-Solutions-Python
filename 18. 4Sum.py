class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        - Brute force solution is to use 4 nested loops to find all unique quadruplets. But it is not time efficient since it takes O(n^4)

        Algo:
            1. Sort the nums arr
            2. Traverse thr the list and pick each index i-th as the first number
            3. Starting another loop at (i + 1)-th from the current index as the second number
            4. Intialize two pointers: left pointer starting from second number's index +1 which is (i + 2)-th index, and right pointer starting from the last index in  the arr. We will find the total sum of four numbers. 
                - If total ==  target, append all four numbers into the result arr
                - If total > target, move right point to left  side(right -= 1)
                - If total < target, move left poitner to right side (left += 1)
                Keep doing it until (left >= right)
                - To avoid duplicates, we move left pointer to the right within the bound until nums[left] != nums[left  - 1]. Similarly, we move right pointer to the left within the bound until nums[right] != nums[right + 1].
            5. Return the res arr
        """

        # sort the arr
        nums.sort()
        res, quad = [], []

        def kSum(k: int, start: int, target: int) -> None:
            # non base case:
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case, two sum II
            left, right = start, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    res.append(quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
        kSum(4, 0, target)
        return res

        # time: O(n^(k - 1)) or O(n^3) for 4SUm. We have k - 2 loops, and twoSum is O(n)
        # Space: O(n)

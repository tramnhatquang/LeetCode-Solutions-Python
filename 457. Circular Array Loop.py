from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # The naive approach is to traverse the whole array and check for each element whether we can form a cycle starting from each element or not. We’ll run a loop on every array element and keep track of the visited element using an additional array. We’ll check the condition for both the forward and backward cycles. If the direction of the cycle changes at any point, we’ll come out of that loop and continue verifying the loop condition for the remaining elements.

        # think about using the slow, and fast pointer
        # 1. Initialize a curr_direction to determine if we are moving forward or backward in the nums arr. If curr_direction = True, we are moving forward, otherwise, if its False, we are moving backward.
        # 2. If the abs(nums[i]) == len(nums) -> we have a loop with one element and taking a steap here means returning to the same location
        # 3. we set slow = fast = curr_index
        # REFER TO https://www.educative.io/module/page/8q5JgjuQREjpzD9gq/10370001/4803867293515776/5658756559142912
        curr_direction = None
        n = len(nums)

        for i in range(n):
            if abs(nums[i]) == n:
                continue

            # True if moving forward. False for moving backward
            curr_direction = nums[i] >= 0
            slow = fast = i

            while slow != fast or slow != -1 or fast != -1:
                # move slow pointer 1 step head, fast pointer 2 steps ahead
                slow = self.next_step(nums, slow, curr_direction)
                if slow == -1:
                    break

                fast = self.next_step(nums, fast, curr_direction)
                if fast != -1:
                    fast = self.next_step(nums, fast, curr_direction)

                if fast == -1 or slow == fast:
                    break

            if slow == fast and slow != -1:
                return True
        return False

    def next_step(self, nums: List[int], curr_index: int, curr_direction: bool) -> int:
        next_direction = nums[curr_index] >= 0

        if (next_direction != curr_direction or abs(nums[curr_index] % len(nums)) == 0):
            return -1
        find_step = (curr_index + nums[curr_index]) % len(nums)
        return find_step

        # time: O(n^2), space: O(1)

from typing import *

from TreeNode import *


def getSumRightLeafs(root: TreeNode) -> int:
    if not root:
        return 0
    if root.right and not root.right.left and not root.right.left:
        return root.right.val + getSumRightLeafs(root.left)
    else:
        return getSumRightLeafs(root.left) + getSumRightLeafs(root.right)


def max_sum_profit(nums: List[int], k) -> int:
    # process the first k elements
    # this is a problem from a company called Tarana Wireless Online Assessment
    curr_sum = max_sum = 0
    left = 0
    for right in range(len(nums)):
        # maintain window length == k
        curr_sum += nums[right]
        if right - left + 1 > k:
            curr_sum -= nums[left]
            left += 1
            # update max_sum
            max_sum = max(max_sum, curr_sum)

    return max_sum


def gex_max_aggregate_temperature_change(arr: List[int]) -> int:
    # similar to max sum of sub-arrays
    # Redo the problem from Amazon Online Assessment
    curr_max = arr[0]
    global_max = float('inf')
    for num in arr[1:]:
        curr_max = max(num, curr_max + num)
        global_max = max(global_max, curr_max)

    return global_max


# time: O(n), n is length of arr


if __name__ == '__main__':
    # all the test cases are done in a different file
    pass

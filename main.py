from typing import *


def max_sum_profit(nums: List[int], k) -> int:
    # process the first k elements
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


if __name__ == '__main__':
    pass
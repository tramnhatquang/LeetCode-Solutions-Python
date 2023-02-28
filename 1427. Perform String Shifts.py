import math
from typing import *

   def stringShift_optimal(self, s: str, shift: List[List[int]]) -> str:
        """
        The second approach is to calculate the net shifting
        we know if we have [0, 5], [1, 5] -> FIrst, we shift left by 5 steps then shift right by 5 steps. That means the arr remains the same
        We can think of calculating the net shifting. SO basically, we traverse thr the shift arr. let's call net_shift = 0
            - If direction == 0, net_shift -= amount
            - If direction == 1, net_shift += amount

        At the end, if net_shift > 0, we need to shift the original arr to the right by net_shift steps, and vice verse
        """

        net_shift = 0
        n = len(s)
        for direction, amount in shift:
            # amount %= n
            if direction == 0:
                net_shift -= amount
            else:
                net_shift += amount
        print(f'Net shift: {net_shift}')

        net_shift %= n
        return s[-net_shift:] + s[:-net_shift]

        # time: O(n + l), spacE: O(l)

    def stringShift_brute_force(self, s: str, shift: List[List[int]]) -> str:
        """
        Approach 1: DO a stimulation based on the shift arr
        - If direction  == 0, do a left shift by amount steps
        - If direction == 1, do a right shift by amount steps
        """
        for direction, amount in shift:
            amount %= len(s)  # if the shift about == len(string), the arr remains the same
            if direction == 0:  # left shift
                s = s[amount:] + s[:amount]
            else:
                s = s[-amount:] + s[:-amount]
        return s
        # time: O(n * L) where n is length of shift arr, L is length of the string
        # spacE: O(L) since everytime we shfit, we create a new string

# a = -2
# a %= 5
# print(a)
# print(math.fmod(-2, 5))
# abcde -> cdeab

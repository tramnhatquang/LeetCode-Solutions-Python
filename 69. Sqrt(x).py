class Solution:
    def mySqrt(self, x: int) -> int:
        """
        A square root of a number x goes from 0 to x // 2 (inclusively). Let say a is x squared root
        0 < a <= x / 2
        """
        # base case: sqrt(0) = 0, sqrt(1) = 1
        if x <= 1:
            return x

        # do a binary search from 2 to x/2 (inclusively)

        left, right = 2, x//2
        while left <= right:
            mid = (left + right) // 2
            product = mid * mid
            if product == x:
                return mid
            elif product > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
        # time: O(log n)
        # space: O(1)

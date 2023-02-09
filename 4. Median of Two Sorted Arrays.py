class Solution:

    def findMedianSortedArrays_optimal(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # if A is greater than B , then switch them so that A is always smaller arr
        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

    def findMedianSortedArrays_brute_force(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force solution
        """
            1. Append all numbers into a result arr
            2. Sort all the arrays
            3. Find the median value
        """
        res = []
        for num in nums1:
            res.append(num)
        for num in nums2:
            res.append(num)
        res.sort()

        n = len(res)
        if n % 2:  # odd
            return res[n // 2]
        # sum of two middle values
        total = res[n // 2] + res[n // 2 - 1]
        return total / 2

        # time: O((m + n)log(m + n))
        # space: O(m + n) created by the result arr

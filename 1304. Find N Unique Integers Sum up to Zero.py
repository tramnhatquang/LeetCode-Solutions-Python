class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)

        if n % 2:  # if n is odd
            res.append(0)
        return res
        # time: O(n)
        # space: O(n)

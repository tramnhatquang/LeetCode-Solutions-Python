class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        res = [-1] * n
        # since the last element has -1 as its max
        # to keep track the curr max so far up up to i-th index (not inlcuding i-th index)
        curr_max = -1
        for i in range(n - 1, -1, -1):
            res[i] = curr_max
            # update the curr max before proceeding to the next max
            if curr_max < arr[i]:
                curr_max = arr[i]

        return res

        # time: O(n) = space, n is length of arr

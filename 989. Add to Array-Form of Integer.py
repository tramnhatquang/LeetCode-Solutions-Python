class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        Traverse from end of the arr to the front that means from (nums.length - 1) index to 0 index, 
            - Update nums[i] = (k + nums[i]) % 10
            - Update k = k // 10
        After reach the first index, if k != 0, then update arr as [k] + arr
        """
        n = len(num)
        # treat k as a carry
        for i in range(n - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)

        if k: # if we still have a carry
            return [int(i) for i in str(k)] + num
        return num

        # since 1 <= k <= 10^4 -> it does not matter much
        # time: O(n)
        #space: O(1)


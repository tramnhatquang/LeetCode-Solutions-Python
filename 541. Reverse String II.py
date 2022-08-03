class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Approach 1: Using slicing index
        # time = space =  O(n), n is the length of s
        a = list(s) # O(n)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return "".join(a)

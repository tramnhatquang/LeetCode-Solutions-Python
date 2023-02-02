class Solution:
    def gcdOfStrings_optimal(self, str1: str, str2: str) -> str:
        # more elegant, mathematical Solution
        # check if they have non-zero GCD String
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of two lengths
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
        # time = space = O(m + n)

        # 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # brute force Solution
        #  try to look for longest prefix substring for both strings
        # 1. Starting with the shorter string among those two. Check if the current one is a substring in the other one
        # 2. If it is not, I continue removing the last character from the base and continuing comparing

        # If base is the GCD string, then str1 and str2 are made of multiple of base, so we just check if len(str1) and len(str2) can be made up of multiple base concatenations. We first check if the length of str is divisible by the length of base.
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k > 0 or len2 % k > 0:
                return False
            # at here, both strings are divisible by k
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0,  -1):
            if valid(i):
                return str1[:i]
        return ""

        # time: O(min(m, n)*(m+ n)) where m, n are lengths of str1, str2
        # space: O(min(m, n))

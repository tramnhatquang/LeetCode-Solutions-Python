class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        """
        Brute force solution is to try all possible substrings and check if they are palindromic (TC is O(n^3) and not time efficient)

        We can optimize the TC to O(n^2) by using two pointers technique
        The question is something similar to find the largest length of palindromic substring in a string
        Algo:
            1. Initialize a left, right pointer to each char in string s
            2. Try to expand left pointer to the left, right pointer to the right as much as possible. If s[left] == s[right] we can increase the count
                - Take care of the case when a palindromic substring has odd or even length. For example, i.e aaab, abcbad
        """
        n = len(s)
        count = 0
        for i in range(n):
            # odd length
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count

        # time: O(n^2), spacE: O(1)

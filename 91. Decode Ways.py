class Solution:
    
    def numDecodings_top_down(self, s: str) -> int:
        """
        Recursion with memoization
        """
        memo = {}

        def backtrack(start_index: int) -> int:
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return 1
            ans = 0
            if s[start_index] == '0':
                return 0
            # decode one digit
            ans += backtrack(start_index +  1)

            # decode two digits
            if (10 <= int(s[start_index: start_index + 2]) <= 26):
                ans += backtrack(start_index + 2)

            # record in the memo
            memo[start_index] = ans
            return ans
        return backtrack(0)    
        # time = space = O(n)
    
    def numDecodings_brujte_force(self, s: str) -> int:
        """
        - Edge case: if we have a string has a leading zero (i.e 06), we cannot decode it. 
        - Each digit 1-9 maps to an alphabet. For digits 1 and 2 there is a possibility to decode two consecutive digits together.
        """

        def backtracking(start_index: int) -> int:
            if start_index == len(s): # base case
                return 1
            ans = 0 # initial state

            # we cannot decode a string that has a leading zero
            if s[start_index] == '0':
                return 0
            # decode one digit
            ans += backtracking(start_index + 1)

            # decode two string
            if (10 <= int(s[start_index: start_index + 2]) <= 26):
                ans+= backtracking(start_index + 2)

            return ans
        return backtracking(0)

        # time: O(2^n) for each node it contains two more approaches
        # space: O(1)
        # this approach is TLE




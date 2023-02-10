class Solution:
    
    def fib_bottom_up(self, n: int) -> int:
        if n <= 1:
            return n
        # bottom up, tabulation

        arr = [None] * (n + 1)
        arr[0], arr[1] = 0, 1 # base cases

        for i in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]

        # time = space = O(n)
        
    def fib_top_down(self, n:int) -> int:
        # use memoization by storing the expensive calls into the hash map and retrieve it immediately if needed without re-calculating the calls

        memo = {}

        def dp(i: int) -> int:
            """
            dp(i) denotes the number at i-th position in the Fibonacci sequence
            """
            if i <= 1:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)

    def fib_recursive_without_memoization(self, n: int) -> int:
        # n = 0 -> fib(0) = 0
        # n = 1 -> fib(1) = 1
        # f(n) = f(n -1 ) + f(n-2) if n > 1
        # use recursion without memoization
        # it costs TLE

        # establish the base cases
        if n < 2:
            return n

        return self.fib_recursive_without_memoization(n - 1) + self.fib_recursive_without_memoization(n - 2)

# time: O(2^n), space: O(n)

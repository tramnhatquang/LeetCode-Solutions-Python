import math


class Solution:
    

    def numSquares_bfs_greedy(self, n):

        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level
    
    def numSquares_bottom_up(self, n: int) -> int:
        """
        Think about using Dynamic Programming to solve this problem
        12 = 9 + 3 = 9 + 1 + 1 + 1
        12 = 4 + 4 +4 

        The important recurrence realtion is that dp[i] = min(dp[i - k] + 1) where k is all possible perfect squares that is less than or equal to original number, i can go from 1 to n + 1

        """
        # using DP bottom-up approach
        dp = [n] * (n + 1)
        dp[0] = 0 # base case since there is no perfect squares adding up to 0

        squares = set([i**2 for i in range(1, int(math.sqrt(n)) + 1)])
        for i in range(1, n + 1):
            for square in squares:
                if i**i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]

        # time: O(n* sqrt(n)), outer loop runs in n times, the inner loop runs in sqrt(n) times
        # space: O(n)
    
    def numSquares_brute_force(self, n: int) -> int:
        """
        Brute force solution:
            - Generate all perfect squares that is less than or equal to n, then use a greedy approach
            - Find all combinations of square that add up to n, and return the minimal one of them

        NOTE: CANNOT USE greddy approach 
        ex: 12 = 9 + 3 = 9 + 1 + 1 + 1 -> min(12) = 4
        or 12 = 4 + 4 + 4 -> min(12) = 3
        If we use greedy, we will return 4 but that's not a correct approach
        """
        # we use set to increase the look up time
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)
        # time: TLE, not time efficient, 


print([i**2 for i in range(1, int(math.sqrt(12)) + 1)])
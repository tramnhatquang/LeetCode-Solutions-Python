class Solution:

    def uniquePaths_optimal_space(self, m: int, n: int) -> int:

        # optimal space Solution
        if m == 1 or n == 1:
                return 1

            # since we only need to use the previous row and curr row to compute
            # we can optimize the space complexity to O(n)
            dp = [1] * n
            for i in range(1, m):
                for j in range(1, n):
                    dp[j] += dp[j - 1]

            return dp[n - 1]
    
            # time: O(m * n), space= O(n)
        """
        The hardest part in his solution is dp[j] = dp[j] + dp[j-1]

Think the first dp[j] is the square you are trying to calculate (aka square[i][j]). The second dp[j] is the square above it (aka square[i-1][j]). The dp[j-1] is the one on the left (aka square[i][j-1]).
        """

    def uniquePaths_no_optimal_space(self, m: int, n: int) -> int:
        """
        Since robot can move either down or right, there is only one path to reach the cells in the first row: right->right->...->right. 

        The same is valid for the first column, though the path here is down->down-> ...->down.

        What about the "inner" cells (m, n)? To such cell one could move either from the cell on the left (m, n - 1), or from the cell above (m - 1, n). That means that the total number of paths to move into (m, n) cell is uniquePaths(m - 1, n) + uniquePaths(m, n - 1).

        Recursive approach with TLE:
        class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        """

        # rewrite the recursive approach using DP

        """
        Algo:
            1. Initialize 2d array d[m][n] = number of paths to (m, n) cells. To start, put number of paths equal to 1 for the first row and the first column. Fodr the simplicity, one could Initialize the the whole 2d arr by ones
            2. Iterate over all inner cells: dp[row][col] = dp[row][col-1] + 
        dp[row - 1][col]
            3. Return dp[m - 1][n - 1]

        """
        dp = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c-1]

        return dp[m - 1][n - 1]

        # time: O(m * n) = space

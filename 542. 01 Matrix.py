import copy
class Solution:
    
    def updateMatrix_optimal(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Use DP approach to solve this problem 
        The min distance to a one-value cell = min distance of its 4 connected cells
        In this problem, a cell has at most 4 neighbors that are left, top, right, bottom. If we use dynamic programming to compute the distance of the current cell based on 4 neighbors simultaneously, it's impossible because we are not sure if distance of neighboring cells is already computed or not.
That's why, we need to compute the distance one by one:
    - Firstly, for a cell, we restrict it to only 2 directions which are left and top. Then we iterate cells from top to bottom, and from left to right, we calculate the distance of a cell based on its left and top neighbors.
    - Secondly, for a cell, we restrict it only have 2 directions which are right and bottom. Then we iterate cells from bottom to top, and from right to left, we update the distance of a cell based on its right and bottom neighbors.
        """
        ROWS, COLS = len(mat), len(mat[0])
        # find the min(top, left) of each 1-val cells
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] != 0: # only update 1-value cell
                    top = mat[row - 1][col] if row >0 else float('inf')
                    left = mat[row][col - 1] if col > 0 else float('inf')
                    mat[row][col] = min(top, left) + 1

        # Go from bottom to top, from right to left
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS -1, -1, -1):
                if mat[row][col] != 0:
                    right = mat[row][col + 1] if col < COLS - 1 else float('inf')
                    bottom = mat[row + 1][col] if row < ROWS - 1 else float('inf')
                    mat[row][col] = min(min(bottom, right) + 1, mat[row][col])
        
        return mat

        # time: O(m * n), m, n are number of rows, cols respectively
        # space: O(1), since we modify the given input


    
    def updateMatrix_bfs(self, mat: List[List[int]]) -> List[List[int]]:
        res = copy.deepcopy(mat)

        ROWS, COLS = len(mat), len(mat[0])
        queue = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if res[r][c] == 0:
                    queue.append((r, c))
                else:
                    res[r][c] = -1 # marked as not process yet
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # print(f'Queue: {queue}')


        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    if res[new_row][new_col] == -1:
                        res[new_row][new_col] = res[row][col] + 1
                        # append to the queue
                        queue.append((new_row, new_col))
        return res

        # time: O(m * n) = space, m, n are number of rows, number of columns respectively
        

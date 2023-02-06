class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use recursion, dfs, backtracking to solve this problem
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(index: int, row: int, col: int) -> bool:
            if index == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or word[index] != board[row][col] or (row, col) in visited):
                return False

            visited.add((row, col))
            res = dfs(index + 1, row + 1, col) or dfs(index + 1, row - 1,
                col) or dfs(index + 1, row, col - 1) or dfs(index + 1, row, col + 1)
            visited.remove((row, col))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        return False
        # time: O(N * 3^ L), n is the number of cells in the board, L is length of word to be matched

from collections import *
from typing import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach 1: Set of rows, columns, and sub-boxes
        #   - Check if any rows or columns contain duplicate numbers
        #   - Check if any sub-boxes contain duplicate numbers
        #       - each sub-box has row index of (i // 3) and column index of (j // 3) for a specific cell at (i, j)-th index.
        #   - Use three dictionaries to check these above conditions, where keys denote the row/col index, values are set of all the numbers in a row/col/sub-box

        rows, cols, squares = collections.defaultdict(
            set), collections.defaultdict(set), collections.defaultdict(set)

        for row in range(9):
                for col in range(9):
                    # check duplicate in row, col, and 3x3 boxes
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in cols[col]:
                        return False
                    if board[row][col] in squares[(row // 3, col // 3)]:
                        return False

                    # add the curr cell into the row, col, and the squares
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[(row//3, col//3)].add(board[row][col])

        return True
            # time:O(81) = O(1)
            # space: O(81) = O(1)

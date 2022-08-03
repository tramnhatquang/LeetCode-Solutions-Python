from collections import *
from typing import *


class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		# approach 1: Set of rows, columns, and sub-boxes
		#   - Check if any rows or columns contain duplicate numbers
		#   - Check if any sub-boxes contain duplicate numbers
		#       - each sub-box has row index of (i // 3) and column index of (j // 3) for a specific cell at (i, j)-th index.
		#   - Use three dictionaries to check these above conditions, where keys denote the row/col index, values are set of all the numbers in a row/col/sub-box

		rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(
			set)

		# traverse through each cell in the sudoku board
		for r in range(len(board)):
			for c in range(len(board[0])):
				if board[r][c] == '.':
					continue
				# check duplicates in rows, cols and sub-box
				if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][
					c] in squares[(r // 3, c // 3)]:
					return False

				# add the number to specific row, col, squares
				rows[r].add(board[r][c])
				cols[c].add(board[r][c])
				squares[(r // 3, c // 3)].add(board[r][c])

		return True

# time: O(1) = space since we only have 81 cells (9x9)

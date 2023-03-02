class TicTacToe:
	"""
	- The optimal solution is to find the winner in O(1). Basically, we have to check a winner in O(1) when he or she has done marking an entire rwo, column, diagonal, and anti diagonal cells
	- SInce we have an n x n board, the winner has to marked n times for a certain row, column, diagonal or anti-diagonal line.
	- Algo:
		1. BUild arrays of rows, columns, of size n. Intialize diagonal = anti_diagonal =0
	"""

	def __init__(self, n: int):
		self.rows = [0] * n
		self.cols = [0] * n
		self.diagonal = 0
		self.anti_diagonal = 0

	def move(self, row: int, col: int, player: int) -> int:
		curr_player = 1 if player == 1 else -1
		self.rows[row] += curr_player
		self.cols[col] += curr_player

		n = len(self.rows)
		# check if the move is at diagonal line
		if row == col:
			self.diagonal += curr_player
		# check if the move is at the anti-diagonal line
		if row + col == n - 1:
			self.anti_diagonal += curr_player

		# check if the curr player wins
		if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(
				self.anti_diagonal) == n:
			return player

		# no one wins
		return 0

# time: O(1)
# space: O(n) because we use arrays rows, cols of size n

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

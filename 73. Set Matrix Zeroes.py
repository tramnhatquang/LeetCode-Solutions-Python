class Solution:
	class Solution:
		def setZeroes_optimal(self, matrix: List[List[int]]) -> None:
			"""
			Do not return anything, modify matrix in-place instead.
			"""

			# use the first cell of each row and column as a flag to indicate whether a row or a column must be set to zero
			rows, cols = len(matrix), len(matrix[0])

			is_first_col_zero = False
			for r in range(rows):
				# since the first cell for both first row and first column is the same
				# i.e. matrix[0][0]
				# we use matrix[0][0] to check whether the first row should be set to zero
				# and use is_first_col_zero to check whether the first column should be set to zero
				if matrix[r][0] == 0:
					is_first_col_zero = True
				for c in range(1, cols):
					if matrix[r][c] == 0:
						# set the first cell of corresponding row and col to 0
						matrix[r][0] = 0
						matrix[0][c] = 0

			for r in range(1, rows):
				for c in range(1, cols):
					if matrix[r][0] == 0 or matrix[0][c] == 0:
						matrix[r][c] = 0

			# see if the first row needs to be set to 0
			if matrix[0][0] == 0:
				for c in range(cols):
					matrix[0][c] = 0

			if is_first_col_zero:
				for r in range(rows):
					matrix[r][0] = 0

	# 0 0 0 0 0
	# 0 3 4 5 0
	# 0 3 5 6 0

	def setZeroes_normal(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# use extra data structure to keep which rows and cols we should set to 0s
		row_set = set()
		col_set = set()
		rows = len(matrix)
		cols = len(matrix[0])
		for r in range(rows):
			for c in range(cols):
				if matrix[r][c] == 0:
					row_set.add(r)
					col_set.add(c)

		# go through again each cell and set it to 0
		for r in range(rows):
			for c in range(cols):
				if r in row_set or c in col_set:
					matrix[r][c] = 0

# time: O(m*n), m is number of rows, n is number of columns
# space: O(m + n)

from typing import *


class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		# approac: flatten the 2d array into 1d arr and use binary search to find the target due to the fact that each row and column is sorted
		# for an m*n arr -> indices are from [0, m*n - 1]
		# row index in 2d = index in 1d // n (the row increases every n indices)
		# col index in 2d = index % n (every n indices, the col resets to 0)

		m, n = len(matrix), len(matrix[0])
		left, right = 0, m * n - 1
		while left <= right:
			mid = (left + right) // 2  # do not care overflow in Python
			row_index = mid // n
			col_index = mid % n

			if matrix[row_index][col_index] == target:
				return True
			elif matrix[row_index][col_index] > target:
				right = mid - 1
			else:
				left = mid + 1

		return False  # if not found

	# time: O(log(m*n)) = O(log m) + O(log n)
	# space: O(1)

	def searchMatrix_alternate(self, matrix: List[List[int]], target: int) -> \
			bool:
		# another way is to do two binary searches on the row first and then the col
		m, n = len(matrix), len(matrix[0])
		top, bottom = 0, m - 1
		# first BST
		while top <= bottom:
			mid_row = (top + bottom) // 2
			if matrix[mid_row][0] > target:
				bottom = mid_row - 1
			elif matrix[mid_row][-1] < target:
				top = mid_row + 1
			else:
				break

		# second BS
		# we cannot find the target
		if top > bottom:
			return False

		# we do BST in the row where the target may be located inside
		left, right = 0, n - 1
		row = (top + bottom) // 2
		while left <= right:
			mid = (left + right) // 2
			if matrix[row][mid] == target:
				return True
			elif matrix[row][mid] > target:
				right = mid - 1
			else:
				left = mid + 1

		return False

# time: O(log(m*n))
# space: O(1)

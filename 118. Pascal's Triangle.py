class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		res = []

		# create all the required rows
		for i in range(numRows):
			row = [None for _ in range(i + 1)]

			# each row will always have the first and last elements are 1s
			row[0] = row[-1] = 1

			# Each triangle element is equal to the sum of the elements
			# above-and-to-the-left and above-and-to-the-right.
			# in other words, res[i][j] = res[i-1][j-1] + res[i-1][j]
			# where i, j are row index and col index respectively and they are inbound

			for j in range(1, len(row) - 1):
				row[j] = res[i - 1][j - 1] + res[i - 1][j]

			# append each row to result List
			res.append(row)

		return res
		# time: O(numRows ^ 2), space: O(1) if we do not count the result output in the space complexity


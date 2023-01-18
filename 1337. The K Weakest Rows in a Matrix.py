class Solution:
	def kWeakestRows_linear_scan(self, mat: List[List[int]], k: int) -> List[int]:
		# Linear search and sort later on
		# Store both the sum of each row and index of it when we traverse thr each row in the 2d arr
		#   - count the number of ones (= sum of each row) in the arr
		#   - also need to store the index of each row into a result arr
		res = []

		for index, row in enumerate(mat):
			res.append((sum(row), index))

		# sort it based on the number of ones and then the index in the descending order
		res.sort()

		# return the index based on the sorted order
		return [index for strength, index in res][:k]

		# time: O(m*n + mlog(m))
		# O(mn) to append strength and index of each row into the arr
		# O(m log (m)) to sort the arr whose length = m
		# space: O(m)


if __name__ == '__main__':
	a = [[1, 2, 3, 4], [5, 6, 7, 8]]
	for i, j in enumerate(a):
		print(i, j)

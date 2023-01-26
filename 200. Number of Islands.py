import collections
from typing import List


class Solution:
	def numIslands_bfs_iterative(self, grid: List[List[str]]) -> int:
		# solve the problem using BFS recursive, and a visited set to track the visited cells
		rows, cols = len(grid), len(grid[0])
		count = 0
		visited = set()

		def bfs(row: int, col: int) -> None:
			queue = collections.deque([(row, col)])
			visited.add((row, col))
			# set the curr cell to 0
			grid[row][col] = '0'

			# traverse thr the queue:
			while queue:
				row, col = queue.popleft()
				for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
					new_row = row + dx
					new_col = col + dy
					if (0 <= new_row < rows and 0 <= new_col < cols) and (new_row, new_col) not in visited and grid[
						new_row][new_col] != '0':
						queue.append((new_row, new_col))
						visited.add((new_row, new_col))
						grid[new_row][new_col] = '0'

		for row in range(rows):
			for col in range(cols):
				if grid[row][col] == '1' and (row, col) not in visited:
					count += 1  # keep track of the number of numIslands
					bfs(row, col)
		return count


def numIslands_dfs_recursive(self, grid: List[List[str]]) -> int:
	rows, cols = len(grid), len(grid[0])
	count = 0

	def dfs(row, col):
		if not (0 <= row < rows and 0 <= col < cols):
			return
		if grid[row][col] == '0':
			return
		# sinking the current island to 0
		grid[row][col] = '0'
		dfs(row + 1, col)
		dfs(row - 1, col)
		dfs(row, col + 1)
		dfs(row, col - 1)

	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == '1':
				count += 1
				dfs(row, col)
	print(grid)
	return count


# time: O(n), n is the total cells in the arr
# space: O(n), n is the total cells in the arr, and we may visit one cell more than once and memory is not efficient
if __name__ == '__main__':
	s = Solution()
	s.numIslands_bfs_iterative([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
								["0", "0", "0", "1", "1"]])

class Solution:

	def floodFill_BFS_iterative(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		# implement using BFS + queue
		# sanity check
		if image[sr][sc] == newColor:
			return image

		rows, cols = len(image), len(image[0])

		original_color = image[sr][sc]
		image[sr][sc] = newColor

		visited = set()
		queue = collections.deque([(sr, sc)])

		while queue:
			row, col = queue.popleft()
			visited.add((row, col))
			for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				new_row = row + dx
				new_col = col + dy
				if (0 <= new_row < rows and 0 <= new_col < cols) and (image[new_row][new_col] == original_color) and (
						new_row, new_col) not in visited:
					# update color
					image[new_row][new_col] = newColor
					# add them to queue
					queue.append((new_row, new_col))

		return image

	# time: O(N), N is total cells in the 2d-arr
	# space: O(r + c) where r is number of rows, c is number of columns

	def floodFill_dfs_recursive(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		rows, cols = len(image), len(image[0])
		old_color = image[sr][sc]

		if old_color == newColor:
			return image  # no need to do anything

		def dfs(row: int, col: int) -> None:
			# if the (row, col) is invalid or the 4 directionally connected cell is not from the original color
			if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != old_color:
				return

			# replace the old color with new color
			image[row][col] = newColor
			dfs(row + 1, col)  # move to top cell
			dfs(row - 1, col)  # move to bottom cell
			dfs(row, col + 1)  # move to right cell
			dfs(row, col - 1)  # move to left cell

		dfs(sr, sc)  # call the dfs
		return image

# time: O(N), N is number of pixels
# spacE: O(N), this approach is not memory efficient due to the extensive recursive calls and a arbitrary cell can be visited more than once.

# Good approach is to use DFS iterative, or BFS iterative

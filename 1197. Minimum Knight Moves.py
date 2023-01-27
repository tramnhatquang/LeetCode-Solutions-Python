class Solution:

	def minKnightMoves_dp_approach(self, x: int, y: int) -> int:
		@lru_cache(None)
		def DP(x, y):
			if x + y == 0:
				return 0
			elif x + y == 2:
				return 2
			return min(DP(abs(x - 1), abs(y - 2)), DP(abs(x - 2), abs(y - 1))) + 1

		return DP(abs(x), abs(y))

	def minKnightMoves(self, x: int, y: int) -> int:

		# this function returns the next 8 moves from the current pos
		def get_neighbors(coor):
			res = []
			r, c = coor
			delta_row = [-2, -2, -1, -1, 1, 1, 2, 2]
			delta_col = [-1, 1, -2, 2, -2, 2, -1, 1]
			for i in range(len(delta_col)):
				r += delta_row[i]
				c += delta_col[i]
				res.append((r, c))
			return res

		def bfs(node):
			visited = set()
			steps = 0
			queue = deque([node])
			visited.add(node)
			while queue:
				n = len(queue)
				for _ in range(n):
					node = queue.popleft()
					if node == (x, y):
						return steps

					for neighbor in get_neighbors(node):
						if neighbor in visited:
							continue
						queue.append(neighbor)
						visited.add(neighbor)
				steps += 1

		return bfs((0, 0))

# time: O(|x| * |y|)
# space: O(|x| * |y|)

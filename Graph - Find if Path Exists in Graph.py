from typing import *
class Solution:
	def validPath(self, n: int, edges: List[List[int]], source: int,
	              destination: int) -> bool:

		# APPROACH 1: BFS
		# it stores all connected adjacent vertices of a particular vertex
		# time = space = O(V + E)
		#         graph = defaultdict(list)

		#         for vertex1, vertex2 in edges:
		#             graph[vertex1].append(vertex2)
		#             graph[vertex2].append(vertex1)

		#         # use a bfs to find there is a path between source and destination
		#         visited = set()
		#         queue = deque([source])

		#         while queue:
		#             node = queue.popleft()
		#             visited.add(node)
		#             if node == destination:
		#                 return True

		#             # check for all the neighbor
		#             for neighbor in graph[node]:
		#                 if neighbor in visited:
		#                     continue
		#                 queue.append(neighbor)
		#         return False

		# APPROACH 2: DFS
		graph = defaultdict(list)

		for vertex1, vertex2 in edges:
			graph[vertex1].append(vertex2)
			graph[vertex2].append(vertex1)

		stack = [source]
		visited = set()
		while stack:
			node = stack.pop()
			visited.add(node)
			if node == destination:
				return True

			for neighbor in graph[node]:
				if neighbor in visited:
					continue
				stack.append(neighbor)

		return False

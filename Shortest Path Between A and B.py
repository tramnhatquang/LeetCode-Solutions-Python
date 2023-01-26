from collections import deque
from typing import List

"""
Given an (unweighted) connected graph, return the length of the shortest path between two nodes A and B, in terms of the number of edges.

Input:

graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
A = 0
B = 3
Output: 2
"""


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE

	queue = deque([a])
	visited = set([a])
	edge = 0
	while queue:
		curr_length = len(queue)
		for i in range(curr_length):
			node = queue.popleft()
			if node == b:
				return edge
			for neighbor in graph[node]:
				if neighbor in visited:
					continue
				queue.append(neighbor)
				visited.add(neighbor)
		edge += 1

	return edge


# BFS for unweighted graph
# time: O(V + E), V: number of vertices, E is the number of edges
# space: O(V)


if __name__ == '__main__':
	graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
	a = int(input())
	b = int(input())
	res = shortest_path(graph, a, b)
	print(res)

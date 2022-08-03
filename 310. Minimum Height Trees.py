from typing import *
class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		# APPROACH 1: BRUTE-FORCE SOLUTION
		# For each node, we treat each node as a root to build a tree and use DFS to find all the heights. After that, we can find the min heights among them and return all the nodes that return the min heights

		# However, this approach is inefficient due to long time complexity. TC = O(n^2)

		# APPROACH 2: Topologoical Sorting

		# For the tree-alike graph, the number of centroid is no more than 2
		# (Note) The degree of a vertex of a graph is the number of
		# edges incident to the vertex.

		# (Note) A leaf is a vertex of degree 1. An internal vertex is a vertex of
		# degree at least 2.

		# So, we weill remove all the leaf nodes first, then update the degree of all the inner vertices, then remove the new leaves. Continue doing so until the tree has only one of two nodes left.
		# The time and space complexity is O(n), where V = n, and E = n - 1

		# edge cases:
		if n <= 2:
			return [i for i in range(n)]

		# build the graph with all adjacent lists
		neighbors = [set() for i in range(n)]
		for start, end in edges:
			neighbors[start].add(end)
			neighbors[end].add(start)

		# initialize the first layer of leaves
		leaves = []
		for i in range(n):
			if len(neighbors[i]) == 1:
				leaves.append(i)

		# trim all the leaves until reaching the centroids
		remaining_nodes = n
		while remaining_nodes > 2:
			remaining_nodes -= len(leaves)
			new_leaves = []
			# remove the current leaves along with the edges
			while leaves:
				leaf = leaves.pop()
				# find the neighbor of the current leaf
				neighbor = neighbors[leaf].pop()
				# remove the only edge left
				neighbors[neighbor].remove(leaf)
				if len(neighbors[neighbor]) == 1:
					new_leaves.append(neighbor)  # find new leaf

			# prepare for the next round
			leaves = new_leaves

		# the remaining nodes
		return leaves

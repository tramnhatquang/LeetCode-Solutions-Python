import collections


class Solution:
    def validPath_dfs_iterative(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        DFS iterative
        Algo:
        0. we mark all the adjacent nodes to the current node and store them in a hash map
            1. Initialize a bool arr to check if we read the destination from the source
            2. Starting from the source, we pop the top node out of the stack. And check if adjacent node is the destination node
        """
        visited = [False] * n
        visited[source] = True # start from the source
        stack = [source]

        adjacent_map = collections.defaultdict(list)
        for start, end in edges: # bi-directional graph
            adjacent_map[start].append(end)
            adjacent_map[end].append(start)

        while stack:
            node = stack.pop()
            for next_node in adjacent_map[node]:
                if next_node == destination:
                    return True
                if not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node)
        return visited[destination]
        # time: O(n + m), n is number of vertices, m is number of edges
        # spacE: O(n + m)

    def validPath_dfs_recursive(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False] * n
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)
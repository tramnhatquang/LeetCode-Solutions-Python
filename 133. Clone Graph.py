"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Copy as we traverse thr each node in the graph. Without using the hash map, we will go into a cycle and never get out. 
        """
        map_old_new = {}

        def dfs(node: Node) -> Node:
            """
            Return the reference of starting cloned node
            """
            if not node:
                return node
            if node in map_old_new:
                return map_old_new[node]

            cloned = Node(node.val)
            map_old_new[node] = cloned
            for neighbor in node.neighbors:
                cloned.neighbors.append(dfs(neighbor))

            return cloned
        return dfs(node)

        # time: O(V + E), v: number of vertices, e is number of edges
        # spacE: O(v) for the hash map

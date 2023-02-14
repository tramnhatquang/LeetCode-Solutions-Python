class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 - 1

        """
        Append all the gates into the queue and use BFS to find the distance to the nearest gate of each empty room. For first iteration, we pop out the first gate and update the (distance +1) to all adjacent rooms if the cell is valid and cell is empty (INF value)
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(rooms), len(rooms[0])
        queue = collections.deque()
        # append all the gate into the queue, 
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # BFS for each level and update the distance for next adjacent moves
        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                new_row = row + dx 
                new_col = col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if rooms[new_row][new_col] == INF:
                        rooms[new_row][new_col] = rooms[row][col] + 1
                        queue.append((new_row, new_col))
        
        # time: O(m * n), m is number of rows, n is number of cols
        # space: O(1), no extra data structure









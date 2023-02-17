class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        # we start at room 0, mark it True
        visited[0] = True
        
        # do a DFS iteratively using a stack to explore all the rooms
        stack = [0]
        while stack:
            curr_room = stack.pop()
            for next_room in rooms[curr_room]:
                # if we haven't visited the next room
                if not visited[next_room]:
                    visited[next_room] = True
                    stack.append(next_room)
                    
        return all(visited)
    
    # time: O(n + e) where n: number of rooms, e is number of keys 
    # space: O(n)
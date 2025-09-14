class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n
        stack = [0]
        while stack:
            room = stack.pop()
            if not visited[room]:
                visited[room] = True
                for key in rooms[room]:
                    stack.append(key)
        return all(visited)

        
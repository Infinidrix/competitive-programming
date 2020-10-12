class Solution:
    def connect_dots(self, A, x, y, visited):
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        outline = set()
        path = collections.deque()
        path.append((x, y))
        visited.add((x, y))
        while path:
            land = path.popleft()
            for neighbor in neighbors:
                new_x = land[0] + neighbor[0]
                new_y = land[1] + neighbor[1]
                if not (0 <= new_x < len(A) and 0 <= new_y < len(A)): 
                    continue
                    
                if A[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    path.append((new_x, new_y))
                elif A[new_x][new_y] == 0:
                    outline.add((new_x, new_y, 0))
        return outline
        
    def find_one(self, A):
        visited = set()
        for line in range(len(A)):
            for i in range(len(A)):
                if A[line][i] == 1:
                    outline = self.connect_dots(A, line, i, visited)
                    return visited, outline
    def shortestBridge(self, A: List[List[int]]) -> int:
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited, outline = self.find_one(A)
        print(f'Visited: {visited}')
        path = collections.deque()
        path.extend(outline)
        while path:
            point = path.popleft()
            for neighbor in neighbors:
                new_x = point[0] + neighbor[0]
                new_y = point[1] + neighbor[1]
                if not (0 <= new_x < len(A) and 0 <= new_y < len(A)): 
                    continue
                    
                if A[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    print(f"Point: {point}, coords: {(new_x, new_y)}")
                    return point[2] + 1
                elif A[new_x][new_y] == 0 and (new_x, new_y) not in outline:
                    outline.add((new_x, new_y))
                    path.append((new_x, new_y, point[2] + 1))
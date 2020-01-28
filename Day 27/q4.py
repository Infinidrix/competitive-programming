class Solution:
    def __init__(self):
        self.dir = [((0,1), (0, 1)), ((1, 0), (1, 0))]
        self.specials = [((0, 0), (1, -1)), ((0, 0), (-1, 1))]
    
    def mini_moves(self, grid, head, tail, moves, visited):
        if str(head + tail) in visited:
            if visited[str(head + tail)] <= moves:
                return 1000000, visited        
        visited[(str(head + tail))] = moves
        if head == [len(grid) - 1, len(grid) - 1] and tail == [len(grid) - 1, len(grid) - 2]:
            return moves, visited
        min_len = 1000000
        for i in self.dir:
            new_head = [head[0] + i[0][0], head[1] + i[0][1]]
            new_tail = [tail[0] + i[1][0], tail[1] + i[1][1]]
            if 0 <= new_head[0] < len(grid) and 0 <= new_head[1] < len(grid) and 0<= new_tail[0] < len(grid) and 0<= new_tail[1] < len(grid) and grid[new_head[0]][new_head[1]] == 0 and grid[new_tail[0]][new_tail[1]] == 0:
                length, visited = self.mini_moves(grid, new_head, new_tail, moves + 1, visited)
                if length < min_len:
                    min_len = length
        if head[0] + 1 < len(grid) and tail[0] + 1 < len(grid) and grid[head[0] + 1][head[1]] == 0 and grid[tail[0] + 1][tail[1]] == 0 and head[0] == tail[0]:
            i = self.specials[0]
            new_head = [head[0] + i[1][0], head[1] + i[1][1]]
            new_tail = [tail[0] + i[0][0], tail[1] + i[0][1]]
            if 0 <= new_head[0] < len(grid) and 0 <= new_head[1] < len(grid) and 0<= new_tail[0] < len(grid) and 0<= new_tail[1] < len(grid) and grid[new_head[0]][new_head[1]] == 0:
                length, visited = self.mini_moves(grid, new_head, new_tail, moves + 1, visited)
                if length < min_len:
                    min_len = length
        if head[1] + 1 < len(grid) and tail[1] + 1 < len(grid) and grid[head[0]][head[1] + 1] == 0 and grid[tail[0]][tail[1] + 1] == 0 and head[1] == tail[1]:
            # print("been here 3")
            i = self.specials[1]
            new_head = [head[0] + i[1][0], head[1] + i[1][1]]
            new_tail = [tail[0] + i[0][0], tail[1] + i[0][1]]
            if 0 <= new_head[0] < len(grid) and 0 <= new_head[1] < len(grid) and 0<= new_tail[0] < len(grid) and 0 <= new_tail[1] < len(grid) and grid[new_head[0]][new_head[1]] == 0:
                length, visited = self.mini_moves(grid, new_head, new_tail, moves + 1, visited)
                if length < min_len:
                    print("found len3:", length)
                    min_len = length
        return min_len, visited
    
    def minimumMoves(self, grid: List[List[int]]) -> int:
        head = [0, 1]
        tail = [0, 0]
        result = self.mini_moves(grid, head, tail, 0, {})[0]
        if result == 1000000:
            return -1
        return result

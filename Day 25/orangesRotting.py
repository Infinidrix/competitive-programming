# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        
        queue = collections.deque()
        N = len(grid)
        M = len(grid[0])
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    queue.append((i, j))
                  
        while queue:
            curr = queue.popleft()
            for direction in directions:
                new_x = curr[0] + direction[0]
                new_y = curr[1] + direction[1]
                if (0 <= new_x < N and
                    0 <= new_y < M and 
                    grid[new_x][new_y] == 1):
                    grid[new_x][new_y] = grid[curr[0]][curr[1]] + 1
                    queue.append((new_x, new_y))
        max_minutes = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] - 2 > max_minutes:
                    max_minutes = grid[i][j] - 2 
                if grid[i][j] == 1:
                    return -1
        return max_minutes

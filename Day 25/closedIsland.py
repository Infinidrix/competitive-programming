# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def find_zero(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return i, j
        return -1, -1
    
    def dfs(self, grid, x, y):
        if grid[x][y] == 1:
            return True
        is_walled = True
        if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
            is_walled = False
        grid[x][y] = 1
        for i in self.dir:
            new_x = x + i[0]
            new_y = y + i[1]
            if new_x >= 0 and new_x <= len(grid) - 1 and new_y >= 0 and new_y <= len(grid[0]) - 1:
                if not self.dfs(grid, new_x, new_y):
                    is_walled = False
        return is_walled
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        # visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        zero_x, zero_y = self.find_zero(grid)
        while zero_x != -1:
            is_found = self.dfs(grid, zero_x, zero_y)
            if is_found:
                count += 1
            zero_x, zero_y = self.find_zero(grid)
        return count
            
            

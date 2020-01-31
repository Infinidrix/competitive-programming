class Solution:
    def __init__(self):
        self.dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
    
    def dfs(self, grid, curr, max_depth, visited):
        visited.add(str(curr))
        if curr[0] == len(grid)-1 and curr[1] == len(grid)-1: 
            return True
        for i in self.dir:
            new_loc = [curr[0] + i[0], curr[1] + i[1]]
            if (0 <= new_loc[0] < len(grid) and 0 <= new_loc[1] < len(grid) and 
                grid[new_loc[0]][new_loc[1]] <= max_depth and str(new_loc) not in visited and
                self.dfs(grid, new_loc, max_depth, visited)):
                        return True
        return False
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        for i in range(max(grid[0][0], grid[-1][-1]), (len(grid))**2 - 1):
            if self.dfs(grid, [0,0], i, set()):
                return i
        return len(grid)**2 - 1

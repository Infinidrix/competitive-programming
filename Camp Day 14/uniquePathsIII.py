
# https://leetcode.com/contest/weekly-contest-120/problems/unique-paths-iii/

class Solution:
    
    def dfs(self, grid, visited, start, end, zero_count):
        path_count = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        if start == end:
        
            if len(visited) == zero_count + 2:
                return 1
            else:
                return 0
		
        visited.add(start)
        for direction in directions:
            new_i = start[0] + direction[0]
            new_j = start[1] + direction[1]
            new_start = (new_i, new_j)
            
            if (0 <= new_i < len(grid) and 
                0 <= new_j < len(grid[0]) and
                new_start not in visited and
                grid[new_i][new_j] != -1):
                path_count += self.dfs(grid, visited, new_start, end, zero_count)
        
        visited.remove(start)
        return path_count
                
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = -1
        end = -1
        count_zero = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    count_zero += 1
        if start == -1 or end == -1:
            return 0
        return self.dfs(grid, set(), start, end, count_zero)

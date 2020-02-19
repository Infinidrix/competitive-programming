# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_i = [0 for i in range(len(grid))]
        max_j = [0 for i in range(len(grid[0]))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_i[i] = max(max_i[i], grid[i][j])
                max_j[j] = max(max_j[j], grid[i][j])
        
        increase = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                upgrade = min(max_i[i], max_j[j])
                if grid[i][j] < upgrade:
                    increase += upgrade - grid[i][j]
                    
        return increase

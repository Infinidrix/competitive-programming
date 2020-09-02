
# https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0 for i in range(len(grid))]
        col_count = [0 for i in range(len(grid[0]))]
        
        result = 0
        for round in range(1, 3):
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    cell = grid[row][col]
                    if cell == 1:
                        if round == 1:
                            row_count[row] += 1
                            col_count[col] += 1
                        elif row_count[row] > 1 or col_count[col] > 1:
                            result += 1
        return result
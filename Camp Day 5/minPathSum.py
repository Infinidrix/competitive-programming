
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 >= 0 and j - 1 >= 0:
                    sums[i][j] = min(sums[i][j-1], sums[i-1][j])
                elif i - 1 >= 0:
                    sums[i][j] = sums[i-1][j]
                elif j - 1 >= 0:
                    sums[i][j] = sums[i][j-1]
                sums[i][j] += grid[i][j]
        return sums[-1][-1]
                

# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        start = len(grid)
        for i in range(len(grid)):
            if grid[i][-1] < 0:
                start = i
                break
        counts = len(grid) - start
        # print("initial:", counts)
        pos = len(grid[i]) - 2
        while pos >= 0 and start < len(grid):
            while pos >= 0 and grid[start][pos] < 0:
                pos -= 1
                counts += len(grid) - start
                # print("incremented:", counts)
            start += 1
        return counts

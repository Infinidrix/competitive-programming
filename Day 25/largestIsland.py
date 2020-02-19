# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def largestIsland(self, grid: list) -> int:

        visited = set()
        graphs = []
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    graph = set()
                    self.dfs(grid, visited, graph, (i, j))
                    result = max(result, len(graph))
                    graphs.append(graph)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    checked = []
                    local_sum = 0
                    for n in self.dir:
                        new_i = i + n[0]
                        new_j = j + n[1]
                        if (0 <= new_i < len(grid) and
                                0 <= new_j < len(grid[0]) and
                                grid[new_i][new_j] == 1):

                            for g in range(len(graphs)):
                                graph = graphs[g]
                                if (new_i, new_j) in graph and g not in checked:
                                    local_sum += len(graph)
                                    checked.append(g)

                    result = max(local_sum + 1, result)

        return result

    def dfs(self, grid, visited, local_visited, curr):
        local_visited.add(curr)
        visited.add(curr)
        for i in self.dir:
            new_i = curr[0] + i[0]
            new_j = curr[1] + i[1]
            if (0 <= new_i < len(grid) and
                    0 <= new_j < len(grid[0]) and
                    (new_i, new_j) not in visited and
                    grid[new_i][new_j] == 1):
                self.dfs(grid, visited, local_visited, (new_i, new_j))

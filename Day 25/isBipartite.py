
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    
    def dfs(self, grid, curr, subset, visited):
        visited.add(str(curr) + str(subset))
        for i in grid[curr]:
            if str(i) + str(subset) in visited:
                return False
            if str(i) + str(not subset) not in visited and not self.dfs(grid, i, not subset, visited):
                return False
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        for i in range(len(graph)):
            if (str(i)+str(True) not in visited and
                str(i)+str(False) not in visited):
                if not self.dfs(graph, i, True, visited):
                    return False
        return True

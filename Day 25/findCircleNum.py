
# https://leetcode.com/problems/friend-circles/

class Solution:
    
    def dfs(self, graph, node, visited):
        visited.add(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and i not in visited:
                self.dfs(graph, i, visited)
        return 0
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        count = i = 0
        while len(visited) < len(M):
            if i not in visited:
                self.dfs(M, i, visited)
                count += 1
            i += 1
        return count

class Solution:
    
    class graph_node:
        def __init__(self, val):
            self.val = val
            self.neighbours = []
    
    def buildGraph(self, stones):
        shared_cols = {}
        shared_rows = {}
        nodes = []
        for i in stones:
            node = self.graph_node(i)
            nodes.append(node)
            if i[1] in shared_cols:
                for j in shared_cols[i[1]]:
                    j.neighbours.append(node)
                    node.neighbours.append(j)
                shared_cols[i[1]].append(node)
            else:
                shared_cols[i[1]] = [node]
            if i[0] in shared_rows:
                for j in shared_rows[i[0]]:
                    j.neighbours.append(node)
                    node.neighbours.append(j)
                shared_rows[i[0]].append(node)
            else:
                shared_rows[i[0]] = [node]
        return nodes
    
    def dfs(self, node, moves, visited):
        visited.add(str(node.val))
        for i in node.neighbours:
            if str(i.val) not in visited:
                moves = max(moves, self.dfs(i, moves + 1, visited))
        return moves
    
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = self.buildGraph(stones)
        visited = set()
        max_dist = 0
        times = 0
        p = sorted(graph, key = lambda stone: len(stone.neighbours))
        # for i in range(len(graph)):
        i = 0
        visited = set()
        dist = 0
        j = 0
        while len(visited) != len(graph):
            if graph[(i+j)%len(graph)] not in visited:
                dist += self.dfs(graph[(i+j)%len(graph)], 0, visited)
                times += 1
            j += 1
        max_dist = max(max_dist, dist)
        if max_dist == len(graph) - 1:
            return max_dist
            
            
        return max_dist

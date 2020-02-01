# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    class GraphNode:
        def __init__(self, val):
            self.val = val
            self.red_dir = []
            self.blue_dir = []
            
    def bfs(self, node, color, dist, dest):
        node.color = color
        queue = [[node,color,dist]]
        visited = {str(node.val)+str(queue[0][1])}
        while queue:
            if queue[0][1] == 0:
                neighbours = queue[0][0].red_dir
            else:
                neighbours = queue[0][0].blue_dir
            for i in neighbours:
                if str(i.val) + str((queue[0][1]+1)%2) not in visited:
                    queue.append([i, (queue[0][1]+1)%2, queue[0][2]+1])
                    visited.add(str(i.val) + str((queue[0][1]+1)%2))
                    if i.val == dest:
                        return queue[0][2]+1
            queue.pop(0)
        return 1000000
                
                
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        nodes = [self.GraphNode(i) for i in range(n)]
        for i in red_edges:
            nodes[i[0]].red_dir.append(nodes[i[1]])
        for i in blue_edges:
            nodes[i[0]].blue_dir.append(nodes[i[1]])
        dist = [0]
        for i in range(1, n):
            distance = min(self.bfs(nodes[0], 0, 0, i), self.bfs(nodes[0], 1, 0, i))
            if distance == 1000000:
                distance = -1
            dist.append(distance)
        return dist

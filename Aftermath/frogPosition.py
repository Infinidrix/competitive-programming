
# https://leetcode.com/problems/frog-position-after-t-seconds/

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        parent = [0 for i in range(n+1)]
        children = [[] for i in range(n+1)]
        neighbours = [[] for i in range(n+1)]
        
        for edge in edges:
            neighbours[edge[1]].append(edge[0])
            neighbours[edge[0]].append(edge[1])
        
        queue = collections.deque()
        queue.append(1)
        visited = set()
        visited.add(1)
        while queue:
            curr = queue.popleft()
            for i in neighbours[curr]:
                if i not in visited:
                    queue.append(i)
                    children[curr].append(i)
                    parent[i] = curr
                    visited.add(i)
        
        has_children = False
        if children[target]:
            has_children = True
        
        count_prob = 1
        depth = 0
        curr = parent[target]
        while curr != 0:
            count_prob /= len(children[curr])
            curr = parent[curr]
            depth += 1
        
        if (has_children and depth != t) or (not has_children and depth > t):
            return 0
        
        return count_prob
        

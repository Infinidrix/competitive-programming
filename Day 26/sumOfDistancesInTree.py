import queue

class Solution:
    
    def make_tree(self, size, edges):
        tree = [[] for i in range(size)]
        for i in edges:
            tree[i[0]].append(i[1])
            tree[i[1]].append(i[0])
        return tree
    
    def compute_child_sum(self, tree, node, result, visited):
        visited.add(node)
        sum_count = children = 0
        for i in tree[node]:
            if i not in visited:
                self.compute_child_sum(tree, i, result, visited)
                children += result[i][1] + 1
                sum_count += result[i][0] + result[i][1] + 1
        result[node] = [sum_count, children]
    
    def fill_result(self, tree, node, child_sum, result, visited):
        que = queue.Queue()
        que.put(node)
        visited.add(node)
        while not que.empty():
            curr = que.get()
            for i in tree[curr]:
                if i not in visited:
                    que.put(i)
                    visited.add(i)
                else:
                    result[curr] = result[i] - child_sum[curr][1] + (child_sum[node][1] - child_sum[curr][1] - 1)
        return visited
    
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = self.make_tree(N, edges)
        child_sum = [0 for i in range(N)]
        self.compute_child_sum(tree, 0, child_sum, set())
        result = [child_sum[0][0] for i in range(N)]
        self.fill_result(tree, 0, child_sum, result, set())
        return result

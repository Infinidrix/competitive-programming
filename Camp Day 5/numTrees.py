
# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def count_trees(self, node_count, checked):
        if node_count in checked:
            return checked[node_count]
        if node_count <= 1:
            return 1
        ways = 0
        for i in range(0, node_count):
            ways += self.count_trees(i, checked) * self.count_trees(node_count - i - 1, checked)
            
        checked[node_count] = ways
        return ways
    
    def numTrees(self, n: int) -> int:
        return self.count_trees(n, {})

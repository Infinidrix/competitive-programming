
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution:
    
    def find_path(self, root, tree, hasApple, checked):
        checked.add(root)
        hasAppleChild = False
        count = 0
        for node in tree[root]:
            if node in checked: continue
            path, temp = self.find_path(node, tree, hasApple, checked)
            if temp:
                count += 2
            count += path
            hasAppleChild = hasAppleChild or temp
        return count, hasAppleChild or hasApple[root]
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = collections.defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
            
        return self.find_path(0, tree, hasApple, set())[0]
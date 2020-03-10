
# https://leetcode.com/problems/time-needed-to-inform-all-employees/


class Solution:
    
    def construct_tree(self, manager_list, inform_list):
        children = [[] for i in range(len(manager_list))]
        for i in range(len(manager_list)):
            if manager_list[i] != -1:
                children[manager_list[i]].append(i)
        return children
    
    def dfs(self, children, manager, informTime):
        time_needed = 0
        if children[manager]:
            time = 0
            for i in children[manager]:
                time = max(time, self.dfs(children, i, informTime))
            time_needed = time + informTime[manager]
        return time_needed
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = self.construct_tree(manager, informTime)
        # print(tree)
        time_needed = self.dfs(tree, headID, informTime)
        return time_needed

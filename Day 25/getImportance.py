"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

# https://leetcode.com/problems/employee-importance/

class Solution:
    
    def sum_importance(self, hash_importance, id, cur_sum):
        for i in hash_importance[id][1]:
            cur_sum = self.sum_importance(hash_importance, i, cur_sum)
        return cur_sum + hash_importance[id][0]
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hash_importance = {}
        for i in employees:
            hash_importance[i.id] = [i.importance, i.subordinates]
        return self.sum_importance(hash_importance, id, 0)

# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution:
    
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cost = 0
        while len(arr) > 1:
            loc = arr.index(min(arr))
            if loc == 0: 
                remove_index = loc + 1
            elif loc == len(arr) - 1 or arr[loc-1] < arr[loc+1]:
                remove_index = loc - 1
            else:
                remove_index = loc + 1 
            cost += arr[remove_index] * min(arr)
            arr.pop(loc)
        return cost


# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        results = [0 for i in range(len(cost) + 1)]
        for i in range(2, len(cost) + 1):
            results[i] = min(results[i-1] + cost[i-1], results[i-2] + cost[i-2])
        return results[-1] 

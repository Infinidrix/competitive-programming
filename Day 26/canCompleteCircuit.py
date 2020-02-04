
# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_cost = [gas[i] - cost[i] for i in range(len(cost))]
        start = 0
        end = 1
        running_sum = 0
        while end != start:
            running_sum += total_cost[end - 1]
            while running_sum < 0:
                running_sum -= total_cost[start]
                start = (start + 1) % len(gas)
            end = (end + 1) % len(gas)
        return start
            

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        count_a = 0
        count_b = 0
        cost = 0
        cost_diff = [[costs[i][0] - costs[i][1], i] for i in range(len(costs))]
        cost_diff = sorted(cost_diff, key = lambda i: abs(i[0]), reverse = True)
        
        for j in range(len(cost_diff)):
            
            if (cost_diff[j][0] > 0 and count_b < len(costs)//2) or count_a >= len(costs)//2:
                count_b += 1
                cost += costs[cost_diff[j][1]][1]
                
            else:
                count_a += 1
                cost += costs[cost_diff[j][1]][0]
        print(count_a, count_b)
        return cost

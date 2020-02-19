# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = [0 for i in range(10001)]
        for i in nums:
            counts[i] += i
        cost_count = [0 for i in range(10001)]
        for i in range(1, len(counts)):
            
            if i - 2 < 0 or cost_count[i-2] + counts[i] > cost_count[i-1]:
                cost_count[i] = cost_count[i-2] + counts[i]
                
            else:
                cost_count[i] = cost_count[i-1]
                
        return cost_count[-1]

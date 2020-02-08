# https://leetcode.com/problems/largest-sum-of-averages/

class Solution:
    def maximize_sum(self, listed, parts, start, checked):
        # print(parts, start)
        if (start, parts) in checked:
            return checked[(start, parts)]
        if parts == 1:
            return sum(listed[start:])/(len(listed) - start)
        summed = 0
        max_avg = 0
        for i in range(len(listed) - start - 1):
            summed += listed[start + i]
            max_avg = max(max_avg, self.maximize_sum(listed, parts - 1, start + i + 1, checked) + summed/(i+1))
        checked[(start, parts)] = max_avg
        return max_avg
            
    
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        return self.maximize_sum(A, K, 0, {})

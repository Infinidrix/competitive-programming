# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sum_total = sum(target)
        target = [-i for i in target]
        heapq.heapify(target)
        while target:
            num = heapq.heappop(target)
            num *= -1
            # print(num, sum_total)
            if num == 1:
                return True
            result = num - (sum_total - num)
            if result > 0:
                heapq.heappush(target, -result)
                sum_total -= num
                sum_total += result
            else:
                return False

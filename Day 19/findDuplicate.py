# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lower = 1
        n = len(nums) - 1
        upper = n
        while lower <= upper:
            mid_point = (lower + upper) // 2
            #print(mid_point, upper, lower)
            count = 0
            count_equal = 0
            for num in nums:
                if num < mid_point:
                    count += 1
                elif num == mid_point:
                    count_equal += 1
                    
            if count_equal > 1:
                return mid_point
            #print("i'm count ", count, (n+1)/2)
            if count < mid_point:
                lower = mid_point + 1
                
            else:
                upper = mid_point - 1
                
        
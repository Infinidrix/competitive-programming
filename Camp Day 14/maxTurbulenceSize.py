
# https://leetcode.com/contest/weekly-contest-120/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        max_length = 0
        curr_length = 0
        sign = None
        
        for i in range(1, len(A)):
            diff = A[i-1] - A[i]
            
            if diff == 0:
                curr_length = 0
                sign = None
                continue
            curr_sign = diff/abs(diff)
            
            if sign == None or sign == curr_sign:
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 1
                
            sign = -curr_sign
            
        return max_length + 1

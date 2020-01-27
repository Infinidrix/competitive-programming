
# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x, n= 1/x, -n
            
        result = 1
        while n > 0:
            i = 1
            temp_res = x
            n -= 1
            while n >= i:
                temp_res **= 2
                n -= i
                i *= 2
            result *= temp_res
        return result

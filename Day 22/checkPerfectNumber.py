import math

# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        addition = 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num%i == 0:
                addition += i + num/i
        return addition + 1 == num
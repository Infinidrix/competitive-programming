# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        first = 0
        second = 1
        third = 1
        for i in range(n-2):
            temp_third = first + second + third
            first = second
            second = third
            third = temp_third
        return third

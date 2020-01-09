# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n != 0:
            n = n // 5
            result += n
        return result
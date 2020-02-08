from math import factorial as fact

# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return fact(m+n-2)//(fact(m-1) * fact(n-1))


# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        checked = [0, 1] + [0 for i in range(n-1)]
        for i in range(2, n+1):
            max_product = 1 if n == i else i 
            for j in range(2, i):
                max_product = max(max_product, checked[j] * checked[i-j])
            checked[i] = max_product
        return checked[-1]

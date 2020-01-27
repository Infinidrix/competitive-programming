
# https://leetcode.com/problems/smallest-integer-divisible-by-k/

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        num = 1
        remainders = []
        for i in range(K):
            res = num % K 
            if res == 0:
                return i + 1
            num = (num%K) * 10 + 1
        return -1

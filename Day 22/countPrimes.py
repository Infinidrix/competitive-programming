
# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [False, False] + [True for i in range(n-2)]
        for i in range(2, n-1):
            if prime[i]:
                j = i**2
                while j <= n-1: 
                    prime[j] = False
                    j += i
        return prime.count(True)
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        twos = n // 2
        ones = n % 2
        ways = 0
        for i in range(twos, -1, -1):
            ways += math.factorial(i+ones)/(math.factorial(ones) * math.factorial(i))
            ones += 2
        return int(ways)

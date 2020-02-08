
# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        copied = 0
        curr = 1
        while n > curr:
            if n % curr == 0:
                count += 1
                copied = curr
                
            count += 1
            curr += copied
        return count

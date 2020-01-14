# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        while A[-1] >= A[-2] + A[-3]:
            A.pop(-1)
            if len(A) < 3:
                return 0
        return A[-1]+A[-2]+A[-3]
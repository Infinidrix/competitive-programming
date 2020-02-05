
# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        status = 0
        for i in range(1, len(A)):
            if status == 0:
                if A[i-1] != A[i]:
                    status = -1 if A[i-1] > A[i] else 1
            elif (A[i-1] < A[i] and status == -1) or (A[i-1] > A[i] and status == 1):
                return False
        return True
            

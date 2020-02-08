
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        checked = {}
        for i in range(len(A)):
            for j in range(len(B)):
                temp = 0
                if A[i] == B[j]:
                    if (i - 1, j - 1) in checked:
                        temp += checked[(i-1, j-1)]
                    temp += 1
                checked[(i, j)] = temp
                
        return max(checked.values())

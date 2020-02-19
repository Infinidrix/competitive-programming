# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        fibs = {}
        max_length = 0
        for k in range(len(A)):
            i = A[k]
            if i in fibs:
                for j in fibs[i]:
                    if i + j[0] not in fibs:
                        fibs[i+j[0]] = []
                    fibs[i+j[0]].append((i, j[1]+1))
                    max_length = max(max_length, j[1] + 1)
            for p in range(k):
                j = A[p]
                if i + j not in fibs:
                    fibs[i+j] = []
                fibs[i+j].append((i, 2))
                     
        return max_length

# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        fibs = {}
        max_length = 0
        
        for k in range(len(A)):
            
            num = A[k]
            if num in fibs:
                for j in fibs[num]:
                    if num + j[0] not in fibs:
                        fibs[num + j[0]] = set()
                    fibs[num + j[0]].add((num, j[1]+1))
                    max_length = max(max_length, j[1] + 1)
                    
            for p in range(k):
                j = A[p]
                if num + j not in fibs:
                    fibs[num+j] = set()
                fibs[num+j].add((num, 2))
                     
        return max_length

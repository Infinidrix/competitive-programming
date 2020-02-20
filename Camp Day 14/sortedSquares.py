
# https://leetcode.com/contest/weekly-contest-120/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        neg_pointer = len(A) - 1
        pos_pointer = len(A)
        for i in range(len(A)):
            if A[i] >= 0:
                pos_pointer = i
                neg_pointer = i - 1
                break
                
        result = []
        while neg_pointer >= 0 or pos_pointer < len(A):
            if neg_pointer >= 0 and pos_pointer < len(A):
                if -A[neg_pointer] > A[pos_pointer]:
                    entry = A[pos_pointer] ** 2
                    pos_pointer += 1
                else:
                    entry = A[neg_pointer] ** 2
                    neg_pointer -= 1
            elif neg_pointer >= 0:
                entry = A[neg_pointer] ** 2
                neg_pointer -= 1
            else:
                entry = A[pos_pointer] ** 2
                pos_pointer += 1
            result.append(entry)
        return result
                

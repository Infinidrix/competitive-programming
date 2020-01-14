# https://leetcode.com/problems/pancake-sorting/
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        moves = []
        while A != []:
            highest = max(A)
            max_index = A.index(highest)
            if max_index == len(A) - 1:
                A.pop()
                continue
            flipped = A[max_index+1:]
            flipped.reverse()
            A = flipped + A[:max_index]
            moves.append(max_index + 1)
            moves.append(len(A) + 1)
        return moves
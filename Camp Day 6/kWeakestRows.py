# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        total_nums = [(sum(mat[i]), i) for i in range(len(mat))]
        sorted_total = sorted(total_nums, key = lambda num: num[0])
        return [i[1] for i in sorted_total[:k]]

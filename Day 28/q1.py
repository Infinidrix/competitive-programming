class Solution:
    
    def move_num(self, index, slot):
        for i in slot:
            if i > index:
                slot.remove(i)
                return i - index
        return -1
    
    def minIncrementForUnique(self, A: List[int]) -> int:
        occ_count = [0 for i in range(40000)]
        for i in A:
            occ_count[i] += 1
        overflow = 0
        i = 0
        count_moves = 0
        while i < len(occ_count):
            if occ_count[i] <= 1: 
                i += 1
                continue
            j = max(i, overflow) + 1
            while j < len(occ_count) and occ_count[j] != 0:
                j += 1
            overflow = j
            count_moves += j - i
            occ_count[i] -= 1
            
        return count_moves

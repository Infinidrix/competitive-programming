
# https://leetcode.com/problems/play-with-chips/

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        evens = len([i for i in chips if i % 2 == 0])
        return min(len(chips) - evens, evens)
        

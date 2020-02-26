
# https://leetcode.com/problems/jump-game-iii/

class Solution:
    
    def can_get_zero(self, arr, start, checked):
        if start in checked or start < 0 or start >= len(arr):
            return False
        if arr[start] == 0:
            return True
        checked.add(start)
        new_index = start + arr[start]
        if self.can_get_zero(arr, new_index, checked):
            return True
        new_index = start - arr[start]
        if self.can_get_zero(arr, new_index, checked):
            return True
    
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.can_get_zero(arr, start, set())

# https://leetcode.com/problems/jump-game-v/

class Solution:
    
    def start_jumping(self, arr, start, moves, checked):
        if start in checked:
            return checked[start]
        max_moves = 1
        curr_max_r = curr_max_l = arr[start]
        for i in range(moves + 1):
            if 0 <= start + i < len(arr) and arr[start] < arr[start + i] and arr[start + i] > curr_max_r:
                max_moves = max(max_moves, self.start_jumping(arr, start + i, moves, checked) + 1)
                curr_max_r = arr[start+i]
            
            if 0 <= start - i < len(arr) and arr[start] < arr[start - i] and arr[start - i] > curr_max_l:
                max_moves = max(max_moves, self.start_jumping(arr, start - i, moves, checked) + 1)
                curr_max_l = arr[start - i]
            
        checked[start] = max_moves
        return max_moves
    
    def maxJumps(self, arr: List[int], d: int) -> int:
        checked = {}
        max_index = 1
        for i in range(len(arr)):
            max_index = max(max_index, self.start_jumping(arr, i, d, checked))
        # print(checked)
        return max_index

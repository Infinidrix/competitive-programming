
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def find_peak(self, A, index_i, index_y):
        if index_i != index_y:
            mid = (index_i + index_y)//2
            
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.find_peak(A, 0, len(A))
    

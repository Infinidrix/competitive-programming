
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort()
        result = []
        current = intervals[0]
        for i in intervals:
            if current[1] >= i[0]:
                current[1] = max(current[1], i[1])
            else:
                result.append(current)
                current = i
        
        result.append(current)
        return result
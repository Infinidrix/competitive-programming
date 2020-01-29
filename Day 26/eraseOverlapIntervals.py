
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        interval = sorted(intervals, key = lambda i: i[1])
        count = 0
        time_min = interval[0][0]
        for i in interval:
            if time_min <= i[0]:
                count += 1
                time_min = i[1]
        return len(intervals) - count

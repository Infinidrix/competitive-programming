# https://leetcode.com/problems/video-stitching/

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        count = 0
        prev_end = 0
        while prev_end < T:
            max_end = prev_end
            for i in clips:
                if i[0] <= prev_end and i[1] > max_end:
                    max_end = i[1]
            if max_end == prev_end:
                return -1
            count += 1
            prev_end = max_end
        return count

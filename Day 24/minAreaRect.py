# https://leetcode.com/problems/minimum-area-rectangle/

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        lines = {}
        for i in points:
            if i[0] not in lines:
                lines[i[0]] = set()
            lines[i[0]].add(i[1])
        x_points = list(lines.keys())
        min_area = 40000**2 + 1
        for i in range(len(x_points)):
            for j in range(i + 1, len(x_points)):
                candidate_lines = list(lines[x_points[i]].intersection(lines[x_points[j]]))
                if len(candidate_lines) <= 1:
                    continue
                candidate_lines.sort()
                min_dist = 40001
                for k in range(1, len(candidate_lines)):
                    diff = candidate_lines[k] - candidate_lines[k-1]
                    if diff < min_dist:
                        min_dist = diff
                area = min_dist * abs(x_points[i] - x_points[j])
                if area < min_area:
                    min_area = area
        if min_area >= 40000**2 + 1:
            return 0
        return min_area
                
            

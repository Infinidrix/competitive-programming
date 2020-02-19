# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines_count = 0
        length = 100
        for i in S:
            if widths[ord(i) - ord("a")] + length > 100:
                lines_count += 1
                length = 0
                
            length += widths[ord(i) - ord("a")]
        return [lines_count, length]

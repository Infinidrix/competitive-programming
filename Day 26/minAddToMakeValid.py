
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        abs_count = 0
        count = 0
        for i in S:
            if i == "(":
                if count < 0:
                    abs_count -= count
                    count = 0
                count += 1
            else:
                count -= 1
        return abs_count + abs(count)

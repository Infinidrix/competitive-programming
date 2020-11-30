
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        grouping = []
        for char in seq:
            if char == "(":
                depth += 1
            grouping.append(depth % 2)
            if char == ")":
                depth -= 1
        return grouping

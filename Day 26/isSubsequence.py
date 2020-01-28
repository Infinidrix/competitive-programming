
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        index = 0
        for i in t:
            if s[index] == i:
                index += 1
                if index == len(s):
                    return True
        return False

#https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_Array = [0 for i in range(26)]
        starter = ord("a")
        for i in range(len(s)):
            count_Array[ord(s[i])-starter] += 1
            count_Array[ord(t[i])-starter] -= 1
        for i in count_Array:
            if i != 0: return False
        return True

# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 1, 0, -1):
            shifts[i-1] += shifts[i]
        
        listed = list(S)
        for i in range(len(listed)):
            listed[i] = chr((ord(listed[i]) - ord("a") + shifts[i]) % 26 + ord("a"))
        return "".join(listed)


# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = []
        for i in range(len(s)):
            diffs.append(abs(ord(s[i]) - ord(t[i])))
        sums = []
        temp_sum = 0
        for i in range(len(s)):
            temp_sum += diffs[i]
            sums.append(temp_sum)
        starting = 0
        length = 0
        for j in range(len(sums)):
            for i in range(starting, len(sums)):
                found = False
                if sums[i] > maxCost:
                    starting = i
                    found = True
                    break
            if found and starting - j > length:
                length = starting - j
            if not found:
                if len(sums) - j > length: 
                    length = len(sums) -j
                break
            maxCost += diffs[j]
        return length
                    
        

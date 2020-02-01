# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        listed = list(s)
        exists = [True for i in range(len(s))]
        counts = 0
        dups = set()
        found = True
        while found:
            found = False
            dups = set()
            counts = 0
            for i in range(len(exists)):
                if not exists[i]: continue
                if listed[i] in dups:
                    counts += 1
                else:
                    dups = set()
                    dups.add(listed[i])
                    counts = 1
                if counts == k:
                    j = -1
                    count = 0
                    while count < k:
                        j += 1
                        if not exists[i-j]: continue
                        count += 1
                        exists[i-j] = False
                    dups = set()
                    counts = 0
                    found = True
        return "".join([listed[i] for i in range(len(listed)) if exists[i]])
                    

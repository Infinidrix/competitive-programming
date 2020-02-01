
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = {}
        for i in arr:
            if i in occurrence:
                occurrence[i] += 1
            else:
                occurrence[i] = 1
        duplicate = set()
        for i in occurrence:
            if occurrence[i] in duplicate:
                return False
            else:
                duplicate.add(occurrence[i])
        return True


# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        counts = {}
        max_count = 0
        max_count_str = ""
        index = 0
        running_string = []
        while index <= len(paragraph):
            if (index == len(paragraph) and len(running_string) != 0) or (index < len(paragraph) and paragraph[index] in "!?',;. "):
                if len(running_string) == 0:
                    index += 1
                    continue
                i = "".join(running_string)
                running_string = []
                i = i.lower()
                if i not in banned:
                    if i not in counts:
                        counts[i] = 0
                    counts[i] += 1
                    if counts[i] > max_count:
                        max_count = counts[i]
                        max_count_str = i
            elif index < len(paragraph):
                running_string.append(paragraph[index])
            index += 1
        return max_count_str
        


# https://leetcode.com/problems/orderly-queue/

class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:    
        listed = list(S)
        if K > 1:
            return "".join(sorted(listed))
        elif K == 0:
            return S
        else:
            mini = listed[:]
            for i in range(len(listed)):
                val = listed[0]
                listed.pop(0)
                listed.append(val)
                if listed < mini:
                    mini = listed[:]
            return "".join(mini)

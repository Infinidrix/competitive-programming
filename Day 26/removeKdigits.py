
# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = list(num)
        i = 1
        while i < len(result) and k > 0:
            if result[i] < result[i-1]:
                # print("popped ", result[i-1])
                result.pop(i-1)
                if i > 1: i -= 1
                k -= 1
            else: i += 1
        result = result if k == 0 else result[:-k]
        return str(int("".join(result))) if result else "0"

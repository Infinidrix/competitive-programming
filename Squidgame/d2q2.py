class Solution:
    def numberOfWays(self, s: str) -> int:
        count1 = count0 = total = total1 = total0 = 0
        for i, c in enumerate(list(map(int, s))):
            if c == 0:
                count0 += 1
                total += total1
                total0 += count1
            else:
                count1 += 1
                total += total0
                total1 += count0
        return total
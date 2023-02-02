class Solution:
    def numberToWords(self, num: int) -> str:
        low = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen"
        mid = "Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred"
        high = "Zero Thousand Million Billion"
        l, m, h = low.split(), mid.split(), high.split()
        has_digit = False
        n = str(num)
        ans = []
        if num == 0:
            return "Zero"
        for i, c in enumerate(n):
            d = int(c)
            if d != 0:
                has_digit = True
            digit = len(n) - i
            if digit % 3 == 2 and d > 1:
                ans.append(m[d])
            if digit % 3 == 1 and i > 0 and n[i - 1] == "1":
                d += 10
            if digit % 3 != 2 and d > 0:
                ans.append(l[d])
            if digit % 3 == 0 and has_digit:
                ans.append("Hundred")
            if digit > 1 and digit % 3 == 1 and has_digit:
                ans.append(h[digit // 3])
                has_digit = False
        return " ".join(ans)
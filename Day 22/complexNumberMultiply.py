# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_expr = a.split("+")
        b_expr = b.split("+")
        a_expr[1] = a_expr[1][:-1]
        b_expr[1] = b_expr[1][:-1]
        res = [int(a_expr[0]) * int(b_expr[0]) - (int(a_expr[1]) * int(b_expr[1])), int(a_expr[0]) * int(b_expr[1]) + (int(a_expr[1]) * int(b_expr[0]))]
        return str(res[0]) + "+" + str(res[1]) + "i"
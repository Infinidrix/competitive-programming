# https://leetcode.com/problems/fraction-addition-and-subtraction

class Solution:
    def GCD(self, a, b):
        if a>b:
            mini = b
            maxi = a
        else:
            mini = a
            maxi = b
        while mini != 0:
            temp = maxi % mini
            maxi = mini
            mini = temp
        return maxi
    
    def add(self, a, b):
        a_num, a_den =[int(i) for i in a.split("/")]
        b_num, b_den = [int(i) for i in b.split("/")]
        res_num = a_num*b_den + a_den*b_num
        res_den = b_den * a_den
        return str(res_num)+"/"+str(res_den)
        
    
    def fractionAddition(self, expression: str) -> str:
        result = "0/1"
        expr = expression.split("+")
        removables = []
        for i in expr:
            if i.count("-") > 0 and i.rindex("-") != 0:
                p = i.split("-")
                for j in range(1, len(p)):
                    p[j] = "-" + p[j]
                if p[0] == "":
                    p.pop(0)
                removables.append(i)
                expr.extend(p)
                print(p)
        for i in removables:
            expr.remove(i)
        print(expr)
        for i in range(len(expr)):
            result = self.add(expr[i], result)
        res_num, res_den = [int(i) for i in result.split("/")]
        gcd = abs(self.GCD(res_num, res_den))

        print(gcd, res_den, res_num)
        return str(res_num//gcd) + "/" + str(res_den//gcd)
        
#  https://leetcode.com/problems/ambiguous-coordinates/

class Solution:
    
    def fill_dots(self, string):
        if len(string) == 1:
            return [string]
        elif string[0] == "0" and string[-1] == "0":
            return []
        elif string[0] == "0":
            return [string[0] + "." + string[1:]]
        elif string[-1] == "0":
            return [string]
        else:
            return [string[: i] + "." + string[i :] for i in range(1, len(string))] + [string]
    
    def ambiguousCoordinates(self, S: str) -> List[str]:
        result = []
        S = S[1:-1]
        for i in range(1, len(S)):
            left_commad = self.fill_dots(S[:i])
            right_commad = self.fill_dots(S[i:])
            if len(left_commad) != 0 and len(right_commad) != 0:
                # print("left:", left_commad, "right:", right_commad)
                result.extend(["(" + i + ", " + j + ")" for i in left_commad for j in right_commad])
        return result

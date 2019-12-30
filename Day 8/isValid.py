class Solution:
    def isValid(self, s: str) -> bool:
        valid_closing = {"(":")", "{":"}", "[":"]"}
        open_valid = ("(", "{", "[")
        opening = []
        for i in s:
            if i in open_valid:
                opening.append(i)
            elif opening and valid_closing[opening[-1]] == i:
                opening.pop()
            else:
                return False
        return opening == []
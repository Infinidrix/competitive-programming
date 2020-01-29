class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        token = tokens
        token.sort()
        points = 0
        while True:
            if token and P >= token[0]:
                points += 1
                P -= token[0]
                token.pop(0)
            elif len(token) > 2 and token[-1]+P >= token[0] and points > 0:
                P += token[-1]
                token.pop()
                points -= 1
            else:
                break
        return points
            

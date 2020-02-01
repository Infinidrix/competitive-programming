
# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True
        stack = [pushed[0]]
        to_push = 1
        for i in popped:
            while not stack or i != stack[-1]:
                if to_push >= len(pushed):
                    return False
                stack.append(pushed[to_push])
                to_push += 1
            stack.pop()
        return True

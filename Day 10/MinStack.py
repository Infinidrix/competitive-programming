class MinStack:
	# https://leetcode.com/problems/min-stack/
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if (not self.min or x<=self.min[-1]):
            self.min.append(x)
        

    def pop(self) -> None:
        check = self.stack.pop(-1);
        if check == self.min[-1]:
            self.min.pop(-1)
        
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
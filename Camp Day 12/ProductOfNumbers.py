# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.additions = [1]
        self.zero_loc = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_loc.append(len(self.additions))
            num = 1
        self.additions.append(self.additions[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.zero_loc and self.zero_loc[-1] >= len(self.additions) - k:
                return 0
        # print(self.additions)
        return int(self.additions[-1] / self.additions[-(k+1)])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

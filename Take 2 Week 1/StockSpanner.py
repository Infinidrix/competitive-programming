
# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.prices = []
        self.days = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        start = len(self.days) - 1
        days = 1
        while start >= 0 and self.prices[start] <= price:
            days += self.days[start]
            start -= self.days[start]
        self.days.append(days)
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        if prices[0] <= prices[1]:
            bought_price = prices[0]
            has_bought = True
        else: 
            bought_price = 0
            has_bought = False
        for i in range(1, len(prices) - 1):
            if prices[i-1] <= prices[i] > prices[i+1] and has_bought:
                profit += prices[i] - bought_price
                bought_price = 0
                has_bought = False
            elif prices[i-1] >= prices[i] < prices[i+1] and not has_bought:
                bought_price = prices[i]
                has_bought = True
        if has_bought and prices[-1] > bought_price:
            profit += prices[-1] - bought_price
        return profit

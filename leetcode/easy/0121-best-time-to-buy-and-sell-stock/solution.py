class Solution(object):
    def maxProfit(self, prices):
        min_value = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] - min_value > profit:
                profit = prices[i] - min_value
        return profit

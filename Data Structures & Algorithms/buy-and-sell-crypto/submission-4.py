class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        
        return profit
        
        
        
        
        
        
        
        
        
        buy, profit = prices[0], 0

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit 
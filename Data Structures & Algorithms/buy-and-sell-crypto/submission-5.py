class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, 102
        for price in prices:
            buy = price if price < buy else buy
            profit = max(profit, price - buy)
        
        return profit


        
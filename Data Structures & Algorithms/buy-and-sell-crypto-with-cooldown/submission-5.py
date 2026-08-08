class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = len(prices)
        if total < 2:
            return 0

        dp = {}
        def findProfit(i, buying):
            if i == total:
                dp[(i, buying)] = 0
                
            if (i, buying) in dp: return dp[(i, buying)]
            skip = findProfit(i+1, buying)
            if buying: # We should Buy or Skip Buying
                buy = findProfit(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, skip)
            else: # We can think of selling or holding
                sell = prices[i] + (findProfit(i+2, not buying) if i+2 <= total else 0)
                dp[(i, buying)] = max(sell, skip)
            return dp[(i, buying)]

        return findProfit(0, True)
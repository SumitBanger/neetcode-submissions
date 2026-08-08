class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = len(prices)
        if total < 2:
            return 0

        dp = {}
        def findProfit(i, buyPrice):
            if i == total:
                dp[(i, buyPrice)] = 0
                
            if (i, buyPrice) in dp: return dp[(i, buyPrice)]
            skip = findProfit(i+1, buyPrice)
            if buyPrice == -1: # We should Buy or Skip Buying
                buy = findProfit(i+1, prices[i])
                dp[(i, buyPrice)] = max(buy, skip)
                return dp[(i, buyPrice)]
            else: # We can think of selling or holding
                sell = (prices[i] - buyPrice) + (findProfit(i+2, -1) if i+2 <= total else 0)
                dp[(i, buyPrice)] = max(sell, skip)
                return dp[(i, buyPrice)]

        return findProfit(0, -1)
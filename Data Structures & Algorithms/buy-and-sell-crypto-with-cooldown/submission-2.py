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

            if buyPrice == -1: # We should Buy or Skip Buying
                buy = findProfit(i+1, prices[i])
                skip = findProfit(i+1, -1)
                dp[(i, buyPrice)] = max(buy, skip)
                return dp[(i, buyPrice)]

            if prices[i] >= buyPrice: # We can think of selling or holding
                sell = (prices[i] - buyPrice) + (findProfit(i+2, -1) if i+2 <= total else 0)
                hold = findProfit(i+1, buyPrice)
                dp[(i, buyPrice)] = max(sell, hold)
                return dp[(i, buyPrice)]
            return 0

        return findProfit(0, -1)
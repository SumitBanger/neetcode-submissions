class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, minTillNow = 1, max(piles), max(piles)
        while left <= right:
            currentRate = (left + right) // 2
            totTimeCurrent = 0
            for pile in piles:
                totTimeCurrent += math.ceil(pile / currentRate)
            
            if totTimeCurrent <= h:
                minTillNow = min(minTillNow, currentRate)
                right = currentRate - 1
            else:
                left = currentRate + 1

        return minTillNow

        
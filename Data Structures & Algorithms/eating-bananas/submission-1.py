import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for val in piles:
                hours += math.ceil(val / mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid -1
                res = min(res, mid)

        return res        
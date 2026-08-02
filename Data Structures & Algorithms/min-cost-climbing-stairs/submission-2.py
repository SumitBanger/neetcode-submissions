class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = len(cost)
        DP = [-1] * (total + 1)
        DP[0], DP[1] = 0, 0
        
        def find_min_cost(n):
            if DP[n] > -1:
                return DP[n]

            DP[n] =  min(find_min_cost(n-1) + cost[n-1], find_min_cost(n-2) + cost[n-2])
            return DP[n]
        
        return find_min_cost(total)

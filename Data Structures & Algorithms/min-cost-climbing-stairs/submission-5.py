class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = len(cost)
        for index in range(total - 2, -1, -1):
            cost[index] += min(cost[index + 1], (cost[index + 2] if index + 2 < total else 0))
        
        return min(cost[0], cost[1])

        # two_before = cost[0]
        # one_before = cost[1]

        # for current in range(2, len(cost)):
        #     temp = one_before
        #     one_before = cost[current] + min(two_before, one_before)
        #     two_before = temp
        # return min(two_before, one_before)

        # total = len(cost)
        # DP = [-1] * (total + 1)
        # DP[0], DP[1] = 0, 0
        
        # def find_min_cost(n):
        #     if DP[n] > -1:
        #         return DP[n]

        #     DP[n] =  min(find_min_cost(n-1) + cost[n-1], find_min_cost(n-2) + cost[n-2])
        #     return DP[n]
        
        # return find_min_cost(total)

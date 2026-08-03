class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Bounds: N -> (0, n)
        Order: small before big -> 0 to n
        '''
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        # DP = [-1] * (n+1)
        # DP[0], DP[1] = 1, 1 

        # def num_ways(N):
        #     if DP[N] > 0:
        #         return DP[N]
        #     DP[N] = num_ways(N-1) + num_ways(N-2)
        #     return DP[N]
        
        # return num_ways(n)
        
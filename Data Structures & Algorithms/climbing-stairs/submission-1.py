class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [-1] * (n+1)
        DP[0], DP[1] = 1, 1 

        def num_ways(N):
            if DP[N] > 0:
                return DP[N]
            DP[N] = num_ways(N-1) + num_ways(N-2)
            return DP[N]
        
        return num_ways(n)
        
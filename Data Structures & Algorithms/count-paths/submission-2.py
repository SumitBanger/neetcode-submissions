class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        def num_ways(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            rightPaths, downPaths = 0,0
            if r+1 < m and c < n:
                rightPaths = num_ways(r+1, c)
            if r < m and c+1 < n:
                downPaths = num_ways(r, c+1)
            dp[r][c] = rightPaths + downPaths
            return dp[r][c]

        # def num_ways(r, c):
        #     if r == m-1 and c == n-1:
        #         return 1
        #     rightPaths, downPaths = 0,0
        #     if r+1 < m and c < n:
        #         rightPaths = num_ways(r+1, c)
        #     if r < m and c+1 < n:
        #         downPaths = num_ways(r, c+1)
        #     return rightPaths + downPaths

        return num_ways(0,0)

        
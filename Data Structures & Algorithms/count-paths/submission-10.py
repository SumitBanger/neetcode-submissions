class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0]*n for _ in range(m)]
        # dp[m-1][n-1] = 1
        '''
        Bounds: r: [0,m-1], c:[0,n-1]
        Order:
            r: big before small -> Loop [m-1 to 0]
            c: big before small -> Loop [n-1 to 0]
        BaseCase: Return 1 when we reach bottom right i.e dp[m-1][n-1] = 1
        '''
        dp_r1 = [0]*(n-1) + [1]
        for r in range(m-1, -1, -1):
            dp_r = [0]*(n)
            for c in range(n-1, -1, -1):
                # Fix: Do not overwrite the destination base case!
                if r == m - 1 and c == n - 1:
                    dp_r[c] = 1
                    continue
                if r+1 < m:
                    dp_r[c] += dp_r1[c]
                if c+1 < n:
                    dp_r[c] += dp_r[c+1]
            dp_r1 = dp_r
        return dp_r1[0]

        # def num_ways(r, c):
        #     if dp[r][c] != -1:
        #         return dp[r][c]
        #     rightPaths, downPaths = 0,0
        #     if r+1 < m and c < n:
        #         rightPaths = num_ways(r+1, c)
        #     if r < m and c+1 < n:
        #         downPaths = num_ways(r, c+1)
        #     dp[r][c] = rightPaths + downPaths
        #     return dp[r][c]

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

        
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def lip(r, c, prev):
            if (r not in range(ROWS)) or (c not in range(COLS)) or matrix[r][c] <= prev:
                return 0

            current = matrix[r][c]
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = 1 + (max(lip(r+1, c, current), 
                            lip(r-1, c, current), 
                            lip(r, c+1, current), 
                            lip(r, c-1, current)))
            return dp[(r, c)]
        
        maxTillNow = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxTillNow = max(maxTillNow, lip(r,c, -1))

        return maxTillNow
        
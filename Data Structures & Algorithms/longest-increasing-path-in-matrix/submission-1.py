class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        #directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = {}

        def lip(r, c, prev):
            if (r not in range(ROWS)) or (c not in range(COLS)):
                return 0

            current = matrix[r][c]
            if current > prev:
                if (r, c) in dp:
                    return dp[(r, c)]
                else:
                    dp[(r, c)] = 1 + (max(lip(r+1, c, current), 
                                    lip(r-1, c, current), 
                                    lip(r, c+1, current), 
                                    lip(r, c-1, current)))
                    return dp[(r, c)]
            return 0
        
        output = []
        for r in range(ROWS):
            for c in range(COLS):
                output.append(lip(r,c, -1))

        print(output)
        return max(output)

        



















'''
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while Q and freshCount > 0:
    timeTillNow += 1
    for index in range(len(Q)): # Perform multi-source BFS
        r, c = Q.popleft()
        for dr, dc in directions:
            row, col = r + dr, c + dc
            if (row in range(ROW)) and (col in range(COL)) and grid[row][col] == 1 and ((row, col) not in visited):
'''
        
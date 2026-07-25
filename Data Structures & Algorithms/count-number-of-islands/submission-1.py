class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        island, visited = 0, set()

        def bfs(r, c):
            Q = deque([(r, c)])
            visited.add((r,c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while Q:
                r, c = Q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROW)) and (col in range(COL)) and grid[row][col] == "1" and ((row, col) not in visited):
                        visited.add((row,col))
                        Q.append((row,col))
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and ((r, c) not in visited):
                    island += 1
                    bfs(r, c)
        
        return island
        
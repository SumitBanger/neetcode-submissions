class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        island, visited, area = 0, set(), 0

        def bfs(r, c):
            Q = deque([(r, c)])
            visited.add((r,c))
            area = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while Q:
                r, c = Q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROW)) and (col in range(COL)) and grid[row][col] == 1 and ((row, col) not in visited):
                        visited.add((row,col))
                        area += 1
                        Q.append((row,col))

            return area
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and ((r, c) not in visited):
                    area = max(area, bfs(r, c))
        
        return area        
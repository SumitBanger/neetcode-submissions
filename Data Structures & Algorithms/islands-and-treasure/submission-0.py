class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        Q, visited = deque(), set()

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0:
                    Q.append((row, col))
                    visited.add((row, col))

        def bfs(distance):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while Q:
                distance += 1
                for index in range(len(Q)):
                    r, c = Q.popleft()
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (row in range(ROW)) and (col in range(COL)) and grid[row][col] != -1 and grid[row][col] == 2147483647 and ((row, col) not in visited):
                            grid[row][col] = distance
                            Q.append((row,col))
                            visited.add((row,col))
                    
        bfs(0)        
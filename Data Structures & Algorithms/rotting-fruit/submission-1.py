class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        Q, visited, timeTillNow, freshCount = deque(), set(), 0, 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2: # This is a Rotting Orange so save its position in Q
                    Q.append((row, col))
                elif grid[row][col] == 1: # This is Fresh Orange -- Keep count of it
                    freshCount += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while Q and freshCount > 0:
            timeTillNow += 1
            for index in range(len(Q)): # Perform multi-source BFS
                r, c = Q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROW)) and (col in range(COL)) and grid[row][col] == 1 and ((row, col) not in visited):
                        Q.append((row,col))
                        visited.add((row,col))
                        freshCount -= 1
        
        return timeTillNow if freshCount == 0 else -1
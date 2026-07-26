class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL, Q, result = len(heights), len(heights[0]), deque(), []
        store = [[0] * COL for _ in range(ROW)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(ROW):
            for col in range(COL):
                if row == 0 or col == 0:
                    store[row][col] += 1
                    Q.append((row, col))
        while Q:
            for index in range(len(Q)):
                r, c = Q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROW)) and (col in range(COL)) and store[row][col] < 1 and heights[row][col] >= heights[r][c]:
                        Q.append((row,col))
                        store[row][col] += 1
        Q = deque()
        for row in range(ROW):
            for col in range(COL):
                if row == ROW - 1 or col == COL - 1:
                    store[row][col] += 2
                    Q.append((row, col))
        while Q:
            for index in range(len(Q)):
                r, c = Q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROW)) and (col in range(COL)) and store[row][col] < 2 and heights[row][col] >= heights[r][c]:
                        Q.append((row,col))
                        store[row][col] += 2

        #print(store)
        for row in range(ROW):
            for col in range(COL):
                if store[row][col] == 3:
                    result.append([row, col])
        return result
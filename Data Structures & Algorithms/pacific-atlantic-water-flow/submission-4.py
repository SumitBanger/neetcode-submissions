class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL, Q, result = len(heights), len(heights[0]), deque(), []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # This solution matches the neetcode.io implementation
        pacific, atlantic = set(), set()
        def dfs(row, col, visited, prevHeight):
            if (row not in range(ROW)) or (col not in range(COL)) or ((row, col) in visited) or (heights[row][col] < prevHeight):
                return
            visited.add((row, col))
            for dr, dc in directions:
                row1, col1 = row + dr, col + dc
                dfs(row1, col1, visited, heights[row][col])       

        for row in range(ROW):
            for col in range(COL):
                if row == 0 or col == 0: dfs(row, col, pacific, heights[row][col])
        for row in range(ROW):
            for col in range(COL):
                if row == ROW - 1 or col == COL - 1: dfs(row, col, atlantic, heights[row][col])
                    
        for row in range(ROW):
            for col in range(COL):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        return result

        # Below is the original solution which i came up myself
        # store = [[0] * COL for _ in range(ROW)]

        # for row in range(ROW):
        #     for col in range(COL):
        #         if row == 0 or col == 0:
        #             store[row][col] += 1
        #             Q.append((row, col))
        # while Q:
        #     for index in range(len(Q)):
        #         r, c = Q.popleft()
        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc
        #             if (row in range(ROW)) and (col in range(COL)) and store[row][col] < 1 and heights[row][col] >= heights[r][c]:
        #                 Q.append((row,col))
        #                 store[row][col] += 1
        # Q = deque()
        # for row in range(ROW):
        #     for col in range(COL):
        #         if row == ROW - 1 or col == COL - 1:
        #             store[row][col] += 2
        #             Q.append((row, col))
        # while Q:
        #     for index in range(len(Q)):
        #         r, c = Q.popleft()
        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc
        #             if (row in range(ROW)) and (col in range(COL)) and store[row][col] < 2 and heights[row][col] >= heights[r][c]:
        #                 Q.append((row,col))
        #                 store[row][col] += 2

        # for row in range(ROW):
        #     for col in range(COL):
        #         if store[row][col] == 3:
        #             result.append([row, col])
        # return result
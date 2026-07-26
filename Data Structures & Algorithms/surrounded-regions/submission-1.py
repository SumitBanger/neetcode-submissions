class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS, visited, Q = len(board), len(board[0]), set(), deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1) and board[row][col] == "O":
                    board[row][col] = "T"
                    Q.append((row, col))
                    visited.add((row, col))
        
        while Q:
            for index in range(len(Q)): # Perform multi-source BFS
                r, c = Q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS)) and (col in range(COLS)) and board[row][col] == "O" and ((row, col) not in visited):
                        board[row][col] = "T"
                        Q.append((row, col))
                        visited.add((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
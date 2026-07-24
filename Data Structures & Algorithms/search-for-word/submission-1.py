class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        res, total, visited = False, len(word), set()

        def dfs(i, row, col):
            nonlocal res
            if i == total:
                res = True
                return
            
            if (row not in range(ROW)) or (col not in range(COL)) or (board[row][col] != word[i]) or ((row, col) in visited):
                return
            visited.add((row, col))
            dfs(i + 1, row, col + 1)
            dfs(i + 1, row, col - 1)
            dfs(i + 1, row + 1, col)
            dfs(i + 1, row - 1, col)
            visited.remove((row, col))

        for row in range(ROW):
            for col in range(COL):
                dfs(0, row, col)
        return res
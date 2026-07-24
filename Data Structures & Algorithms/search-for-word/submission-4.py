class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        found, total, visited = False, len(word), set()

        def dfs(i, row, col):
            if i == total:  return True
            
            if (row not in range(ROW)) or (col not in range(COL)) or (board[row][col] != word[i]) or ((row, col) in visited):
                return
            visited.add((row, col))
            found = (
                dfs(i + 1, row, col + 1) or
                dfs(i + 1, row, col - 1) or
                dfs(i + 1, row + 1, col) or
                dfs(i + 1, row - 1, col)
            )
            visited.remove((row, col))
            return found

        for row in range(ROW):
            for col in range(COL):
                if dfs(0, row, col): return True
        return False
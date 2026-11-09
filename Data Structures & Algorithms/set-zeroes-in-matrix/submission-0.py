class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroRows, zeroCols = [False for _ in range(ROWS)], [False for _ in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    zeroRows[row] = True
                    zeroCols[col] = True
        
        for row in range(ROWS):
            for col in range(COLS):
                if zeroRows[row] or zeroCols[col]:
                    matrix[row][col] = 0
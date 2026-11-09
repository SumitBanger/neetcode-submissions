class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS, zeroFirstRow = len(matrix), len(matrix[0]), False
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row == 0: zeroFirstRow = True
                    else: matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # 2. Second pass: Update the sub-matrix (excluding row 0 and col 0)
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        # 3. Update the first column if the top-left cell was marked zero
        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0
                
        # 4. Update the first row using your tracking variable
        if zeroFirstRow:
            for col in range(COLS):
                matrix[0][col] = 0
        
        # zeroRows, zeroCols = [False for _ in range(ROWS)], [False for _ in range(COLS)]

        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if matrix[row][col] == 0:
        #             zeroRows[row] = True
        #             zeroCols[col] = True
        
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if zeroRows[row] or zeroCols[col]:
        #             matrix[row][col] = 0
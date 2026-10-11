class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS - 1
        while left <= right:
            midRow = (left + right) // 2
            midstartVal, midEndVal = matrix[midRow][0], matrix[midRow][COLS - 1]

            if target == midstartVal or target == midEndVal:
                return True
            elif target < midstartVal:
                right = midRow - 1
            elif target > midEndVal:
                left = midRow + 1
            else:
                colLeft, colRight = 0, COLS - 1
                while colLeft <= colRight:
                    midCol = (colLeft + colRight) // 2
                    midColVal = matrix[midRow][midCol]
                    if target == midColVal:
                        return True
                    elif target < midColVal:
                        colRight = midCol - 1
                    else:
                        colLeft = midCol + 1
                return False
        return False
    
        
        
        
        
        m, n = len(matrix), len(matrix[0])
        left, right, row, col = 0, m-1, -1, -1
        while left <= right:
            midRow = (left+right)//2
            midRowStartVal = matrix[midRow][0]
            midRowEndVal = matrix[midRow][n-1]

            if target == midRowStartVal or target == midRowEndVal:
                return True
            elif target < midRowStartVal:
                right = midRow - 1
            elif target > midRowEndVal:
                left = midRow + 1
            else:
                row = midRow
                break

        if row == -1:
            return False
        
        left, right = 0, n-1
        while left <= right:
            col = (left+right)//2
            midVal = matrix[row][col]

            if target == midVal:
                return True
            elif target < midVal:
                right = col - 1
            elif target > midVal:
                left = col + 1
        
        return False
        

        
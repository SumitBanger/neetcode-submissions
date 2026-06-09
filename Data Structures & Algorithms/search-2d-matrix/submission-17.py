class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right, row, col = 0, m-1, -1, -1
        while left <= right:
            midRow = (left+right)//2
            midRowStartVal = matrix[midRow][0]
            midRowEndVal = matrix[midRow][n-1]

            if target == midRowStartVal or target == midRowEndVal:
                return True
            elif target < midRowStartVal:
                right -= 1
            elif target > midRowEndVal:
                left += 1
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
                right -= 1
            elif target > midVal:
                left += 1
        
        if col == -1:
            return False


        
        
        
        
        rows, cols = len(matrix), len(matrix[0])
        row, left, right = -1, 0, rows - 1
        while left <= right:
            midRow = (left + right) // 2
            startMidRow, endMidRow = matrix[midRow][0], matrix[midRow][cols - 1]
            if target >= startMidRow and target <= endMidRow:
                row = midRow
                break
            elif target < startMidRow:
                right = midRow - 1
            else:
                left = midRow + 1
        
        if row == -1:
            return False

        col, left, right = -1, 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[row][mid]
            if target == midVal:
                return True
            elif target < midVal:
                right = mid - 1
            else:
                left = mid + 1

        return False
        

        
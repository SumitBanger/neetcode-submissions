class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
        
        print(row)

        if row == -1:
            return False

        col, left, right = -1, 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[row][mid]
            if target == midVal:
                col = mid
                break
            elif target < midVal:
                right = mid - 1
            else:
                left = mid + 1

        return False if col == -1 else True
        

        
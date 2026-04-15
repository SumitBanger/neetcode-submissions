class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, left, right = -1, 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        if row == -1:
            return False

        col, left, right = -1, 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                col = mid
                break
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False if col == -1 else True


        
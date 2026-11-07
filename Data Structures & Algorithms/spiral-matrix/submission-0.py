from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS, res = len(matrix), len(matrix[0]), []
        left, right, top, bottom = 0, COLS, 0, ROWS

        while left < right and top < bottom:
            # 1. Iterate Left to Right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Iterate Top to Bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # CRITICAL SAFETY CHECK: Stop if boundaries crossed mid-loop
            if not (left < right and top < bottom):
                break
            
            # 3. Iterate Right to Left (Fixed: bottom - 1)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # 4. Iterate Bottom to Top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res

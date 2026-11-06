class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        
        while left < right:
            # i must track the relative offset within the current layer
            for i in range(right - left):
                top, bottom = left, right
                
                # Perform the 4-way clockwise swap
                (matrix[top + i][right], 
                 matrix[bottom][right - i], 
                 matrix[bottom - i][left], 
                 matrix[top][left + i]) = (matrix[top][left + i], 
                                           matrix[top + i][right], 
                                           matrix[bottom][right - i], 
                                           matrix[bottom - i][left])
            
            # Move to the inner sub-matrix layer
            left += 1
            right -= 1





        
class Solution(object):
    def searchMatrix(self, matrix, target):
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        
        while row_start <= row_end:
            mid_row = row_start + ((row_end - row_start) // 2)
            
            if matrix[mid_row][0] > target:
                row_end = mid_row -1
            elif matrix[mid_row][0] < target:
                row_start = mid_row + 1
            else: 
                return True
        
        print(row_end)
            
        while col_start <= col_end:
            mid_col = ((col_end - col_start) // 2) + col_start
                    
            if (target < matrix[row_end][mid_col]):                
                col_end = mid_col - 1
            elif target > matrix[row_end][mid_col]:
                col_start = mid_col + 1
            elif target == matrix[row_end][mid_col]:
                return True
        
        return False

        
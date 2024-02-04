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
        
        # if the value is not found in any of the rows, it means
        # that the variable row_start holds the position where
        # the value should be inserted to mantain the order, for example:
        # [10, 20, 30, 40] => if i'm searching for 25, the row_start pointer
        # will be at the position 2 (value 30), because it is where i have to insert it
        # keeping the order. However, the row_end points to the position 1 (value 20), and
        # that's the line i'm interested in, hence i use row_end to search in the col
        
        while col_start <= col_end:
            mid_col = ((col_end - col_start) // 2) + col_start
                    
            if (target < matrix[row_end][mid_col]):                
                col_end = mid_col - 1
            elif target > matrix[row_end][mid_col]:
                col_start = mid_col + 1
            elif target == matrix[row_end][mid_col]:
                return True
        
        return False

        
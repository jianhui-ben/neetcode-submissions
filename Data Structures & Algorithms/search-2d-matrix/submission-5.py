class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # """
        # it's a binary search on a a 2d array
        # if we flatten this 2d array into 1d, then we can easily find the index i

        # key is to map each i into the row_i and col_i in the 2d array
        
        # num_rows, num_cols
        # from 1d to 2d:
        #     index i => i // num_cols, i % num_cols
        # from 2d to 1d:
        #     row_i, col_i => row_i * num_cols + col_i
        
        # then we just convert them
        # """
        # num_rows, num_cols = len(matrix), len(matrix[0])
        # def _1d_to_2d(_1d_idx):
        #     return (_1d_idx // num_cols, _1d_idx % num_cols)
        # def _2d_to_1d(row_i, col_i):
        #     return row_i * num_cols + col_i

        # _1d_left, _1d_right = _2d_to_1d(0, 0), _2d_to_1d(num_rows - 1, num_cols - 1)        

        # while _1d_left <= _1d_right:
        #     _1d_mid = _1d_left + (_1d_right - _1d_left) // 2
        #     mid_row_i, mid_col_i = _1d_to_2d(_1d_mid)
        #     if matrix[mid_row_i][mid_col_i] == target:
        #         return True
        #     elif matrix[mid_row_i][mid_col_i] < target:
        #         _1d_left = _1d_mid + 1
        #     else:
        #         _1d_right = _1d_mid - 1

        # left_row_i, left_col_i = _1d_to_2d(_1d_left)
        # if left_row_i >= num_rows or left_col_i > num_cols or matrix[left_row_i][left_col_i] != target:
        #     return False
        # return True
        
        """
        another thought:
        log(num_rows) to find the last num_rows_i where matrix[num_rows_i][0] <= target
        then
        log(num_cols) to find the last num_col_i where matrix[num_rows_i][num_col_i] <= target
        """
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or matrix[right][0] > target: return False
        final_row = right
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[final_row][mid] == target: return True
            elif matrix[final_row][mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or matrix[final_row][right] != target: return False
        return True
        



            
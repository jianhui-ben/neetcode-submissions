class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        classical backtracking
        
        backtracking(cur_board, row_idx)
        """
        
        out = []


        def isValid(row, col, cur_board):
            ## check the col/ upper left / upper right of [row, col]
            for r in range(row):
                if cur_board[r][col] == "Q": 
                    return False

            ## upper left:  [3, 2] -> [2, 1], [1, 0]
            row_col_delta = row - col
            for r in range(row):
                if 0 <= r - row_col_delta < n and cur_board[r][r - row_col_delta] == "Q":
                    return False
            
            ## upper right:  [2, 1] -> [1, 2], [0, 3]
            row_col_sum = row + col
            for r in range(row):
                if 0 <= row_col_sum - r < n and cur_board[r][row_col_sum - r] == "Q":
                    return False
            return True

        def backtracking(cur_board, row_idx):
            if row_idx == n:
                out.append(list(cur_board))
                return
            
            for col in range(n):
                if isValid(row_idx, col, cur_board):
                    cur_board[row_idx] = "." * col + "Q" + "." * (n - col - 1)
                    backtracking(cur_board, row_idx + 1)
                    cur_board[row_idx] = "." * n

        backtracking([[] for _ in range(n)], 0)

        return out
        
        
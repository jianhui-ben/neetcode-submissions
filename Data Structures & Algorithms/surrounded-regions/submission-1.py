class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        dfs to find all the Os that's connecting to the boarder
        """
        ROW, COL = len(board) - 1, len(board[0]) - 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            board[r][c] = "T"
            for del_r, del_c in dirs:
                new_r, new_c = r + del_r, c + del_c
                if 0 <= new_r <= ROW and 0 <= new_c <= COL and board[new_r][new_c] == "O":
                    dfs(new_r, new_c)


        for r in range(ROW + 1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COL] == "O":
                dfs(r, COL)

        for c in range(COL + 1):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROW][c] == "O":
                dfs(ROW, c)
        
        for r in range(ROW + 1):
            for c in range(COL + 1):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        return
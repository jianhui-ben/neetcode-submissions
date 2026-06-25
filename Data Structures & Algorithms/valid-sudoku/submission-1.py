class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## check each row and each coolum
        """
        check each row and each colume 
        
        how to check the small 3 * 3
        
        init 3 arrs for rows, columns, and boxes
        rows[i] save the set of values in board[i]
        columns[i] save the set of values in board[][i]
        boxes[i] save the set of values in board[m][n] where i = (m // 3) * 3 + n // 3
        """
        rows, columns, boxes = [[set() for _ in range(9)] for _ in range(3)]
        
        for m in range(9):
            for n in range(9):
                num = board[m][n]
                if num == ".":
                    continue

                if num in rows[m] or num in columns[n] or num in boxes[(m // 3) * 3 + n // 3]:
                    return False
                rows[m].add(num)
                columns[n].add(num)
                boxes[(m // 3) * 3 + n // 3].add(num)
        
        return True
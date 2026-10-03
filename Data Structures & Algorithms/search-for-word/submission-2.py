class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        for each possible head of the word, do traversal in 3 directions

        traverse(target_idx, cur_row, cur_col, next_possible_directions_set)
        """
        
        self.out = False

        def traverse(target_idx, r, c, next_moves):
            if self.out:
                return
            if target_idx >= len(word):
                self.out = True
                return
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return
            if board[r][c] != word[target_idx]:
                return
            
            temp = board[r][c]
            board[r][c] = "#"
            for del_row, del_col in next_moves:
                ## go right
                if del_row == 0 and del_col == 1:
                    traverse(target_idx + 1, r, c + 1, [(1, 0), (-1, 0), (0, 1)])
                ## go left
                elif del_row == 0 and del_col == -1:
                    traverse(target_idx + 1, r, c - 1, [(1, 0), (-1, 0), (0, -1)])
                ## go down
                elif del_row == 1 and del_col == 0:
                    traverse(target_idx + 1, r + 1, c, [(1, 0), (0, 1), (0, -1)])
                ## go up
                elif del_row == -1 and del_col == 0:
                    traverse(target_idx + 1, r - 1, c, [(-1, 0), (0, 1), (0, -1)])
            board[r][c] = temp

        for r in range(len(board)):
            for c in range(len(board[0])):
                traverse(0, r, c, [(0, 1), (0, -1), (1, 0), (-1, 0)])

        return self.out
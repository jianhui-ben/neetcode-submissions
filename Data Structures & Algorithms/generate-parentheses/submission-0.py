class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        very smart backtracing solution
        
        two conditions:
        as long open_bracket_cnt < n: we could always add "("
        as long as close_bracket_cnt < open_bracket_cnt: we could always add ")"
        """

        out = []
        
        def backtracking(cur_list, open_bracket_cnt, close_bracket_cnt):
            if open_bracket_cnt == close_bracket_cnt == n:
                out.append("".join(cur_list))
                return
            if open_bracket_cnt < n:
                backtracking(cur_list + ["("], open_bracket_cnt + 1, close_bracket_cnt)
            if close_bracket_cnt < open_bracket_cnt:
                backtracking(cur_list + [")"], open_bracket_cnt, close_bracket_cnt + 1)

        backtracking([], 0, 0)

        return out
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        from the boarder to the inland
        """
        pacific_set, atlantic_set = set(), set()
        MAX_R, MAX_C = len(heights) - 1, len(heights[0]) - 1
        
        # for r in range(MAX_R + 1):
        #     for c in range(MAX_C + 1):
        #         if r == 0 or c == 0:
        #             pacific_set.add((r, c))
        #         elif r == MAX_R or c == MAX_C:
        #             atlantic_set.add((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, stored):
            if (r, c) in stored:
                return
            stored.add((r, c))

            cur_height = heights[r][c]
            for del_r, del_c in directions:
                new_r, new_c = del_r + r, del_c + c
                if 0 <= new_r <= MAX_R and 0 <= new_c <= MAX_C and heights[new_r][new_c] >= cur_height:
                    dfs(new_r, new_c, stored)


        ## traverse:
        for r in range(MAX_R + 1):
            dfs(r, 0, pacific_set)
            dfs(r, MAX_C, atlantic_set)
        
        for c in range(MAX_C + 1):
            dfs(0, c, pacific_set)
            dfs(MAX_R, c, atlantic_set)

        return [[a, b] for a, b in pacific_set.intersection(atlantic_set)]





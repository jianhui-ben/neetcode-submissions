class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        for each point, do a dfs
        """

        out = 0

        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def dfs(r, c):
            grid[r][c] = "X"
            for d_r, d_c in dirs:
                new_r, new_c = r + d_r, c + d_c
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)
            return
            


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    out += 1
                    dfs(r, c)
        
        return out

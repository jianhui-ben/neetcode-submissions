class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs to mark the island
        """
        
        self.out = 0
        grid_copy = grid.copy()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = [(r, c)]
            grid_copy[r][c] = -1
            size = 0
            while queue:
                new_queue = []
                for r, c in queue:
                    size += 1
                    for d_r, d_c in dirs:
                        new_r, new_c = d_r + r, d_c + c
                        if 0 <= new_r < len(grid_copy) and 0 <= new_c < len(grid_copy[0]) and grid_copy[new_r][new_c] == 1:
                            new_queue.append((new_r, new_c))
                            grid_copy[new_r][new_c] = -1
                queue = new_queue
            self.out = max(self.out, size)
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid_copy[r][c] == 1:
                    bfs(r, c)
        
        return self.out

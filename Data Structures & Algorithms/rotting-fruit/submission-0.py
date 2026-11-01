from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        typicla BFS
        """
        queue = deque()
        tot_fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    tot_fresh += 1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        out = 0
        while queue:
            r, c, time = queue.popleft()
            for del_r, del_c in dirs:
                new_r, new_c = r + del_r, c + del_c
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                    new_time = time + 1
                    tot_fresh -= 1
                    out = max(out, new_time)
                    queue.append((new_r, new_c, new_time))
                    grid[new_r][new_c] = 2
        return out if not tot_fresh else -1
                    
        